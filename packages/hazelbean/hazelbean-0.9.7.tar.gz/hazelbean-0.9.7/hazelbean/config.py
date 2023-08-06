# coding=utf-8
import os, sys, math, time
from osgeo import gdal, ogr, osr
from gdal import gdalconst
import numpy
import numpy as np
import logging
import warnings
import traceback
import multiprocessing
from collections import OrderedDict
import hazelbean as hb
import inspect

# First check for config file specific to this computer
user_path = os.path.expanduser('~')
default_hazelbean_config_uri = os.path.join(user_path, 'documents/hazelbean/config.txt')
PRIMARY_DRIVE = 'c:/'
EXTERNAL_BULK_DATA_DRIVE = 'e:/'
if os.path.exists(default_hazelbean_config_uri):
    with open(default_hazelbean_config_uri) as f:
        for line in f:
            if '=' in line:
                line_split = line.split('=')
                if line_split[0] == 'primary_drive_letter':
                    PRIMARY_DRIVE_LETTER = line_split[1][0]
                    PRIMARY_DRIVE = PRIMARY_DRIVE_LETTER + ':/'
                if line_split[0] == 'external_bulk_data_drive':
                    EXTERNAL_BULK_DATA_DRIVE_LETTER = line_split[1][0]
                    EXTERNAL_BULK_DATA_DRIVE = EXTERNAL_BULK_DATA_DRIVE_LETTER + ':/'
                if line_split[0] == 'configured_for_cython_compilation':
                    CONFIGURED_FOR_CYTHON_COMPILATION = float(line_split[1])
else:
    CONFIGURED_FOR_CYTHON_COMPILATION = False

# HAZELBEAN SETUP GLOBALS
TEMPORARY_DIR = os.path.join(PRIMARY_DRIVE, 'temp')
BASE_DATA_DIR = os.path.join(PRIMARY_DRIVE, 'onedrive', 'projects', 'base_data')
BULK_DATA_DIR = os.path.join(PRIMARY_DRIVE, 'bulk_data')
EXTERNAL_BULK_DATA_DIR = os.path.join(EXTERNAL_BULK_DATA_DRIVE, 'bulk_data')
HAZELBEAN_WORKING_DIRECTORY = os.path.join(PRIMARY_DRIVE, 'OneDrive\\Projects\\hazelbean\\hazelbean') # TODOO Make this based on config file?
TEST_DATA_DIR = os.path.join(HAZELBEAN_WORKING_DIRECTORY, '../tests/data')
PROJECTS_DIR = os.path.join(PRIMARY_DRIVE, 'OneDrive\\Projects')

TINY_MEMORY_ARRAY_SIZE = 1e+04
SMALL_MEMORY_ARRAY_SIZE = 1e+05
MEDIUM_MEMORY_ARRAY_SIZE = 1e+06
LARGE_MEMORY_ARRAY_SIZE = 1e+07
MAX_IN_MEMORY_ARRAY_SIZE = 1e+011

# FROM Pygeoprocessing 06
LOGGING_PERIOD = 1.0  # min 5.0 seconds per update log message for the module
MAX_TIMEOUT = 60.0
DEFAULT_GTIFF_CREATION_OPTIONS = ['TILED=YES', 'BIGTIFF=IF_SAFER']
LARGEST_ITERBLOCK = 2**20  # largest block for iterblocks to read in cells

# A dictionary to map the resampling method input string to the gdal type
try:
    RESAMPLE_DICT = {
        "nearest": gdal.GRA_NearestNeighbour,
        "near": gdal.GRA_NearestNeighbour,
        "bilinear": gdal.GRA_Bilinear,
        "cubic": gdal.GRA_Cubic,
        "cubic_spline": gdal.GRA_CubicSpline,
        "lanczos": gdal.GRA_Lanczos,
        'mode': gdal.GRA_Mode,
        'average': gdal.GRA_Average,
        'max': gdal.GRA_Max,
        'min': gdal.GRA_Min,
        'med': gdal.GRA_Med,
        'q1': gdal.GRA_Q1,
        'q3': gdal.GRA_Q3,
    }
except:

    RESAMPLE_DICT = {
        "near": gdal.GRA_NearestNeighbour,
        "nearest": gdal.GRA_NearestNeighbour,
        "bilinear": gdal.GRA_Bilinear,
        "cubic": gdal.GRA_Cubic,
        "cubic_spline": gdal.GRA_CubicSpline,
        "lanczos": gdal.GRA_Lanczos,
        "average": gdal.GRA_Average,
        "mode": gdal.GRA_Mode,
    }

resampling_methods = RESAMPLE_DICT


class CustomLogger(logging.LoggerAdapter):
    def __init__(self, logger, *args, **kwargs):
        logging.LoggerAdapter.__init__(self, logger, *args, **kwargs)
        self.L = logger
        self.DEBUG_DEEPER_1_NUM = 9
        logging.addLevelName(self.DEBUG_DEEPER_1_NUM, "DEBUG_DEEPER_1")

    def process(self, msg, kwargs):
        return msg, kwargs

    def debug_deeper_1(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(self.DEBUG_DEEPER_1_NUM):
            self._log(self.DEBUG_DEEPER_1_NUM, message, args, **kws)

    def debug(self, msg, *args, **kwargs):
        for i in args:
            msg += ', ' + str(i)
        msg, kwargs = self.process(msg, kwargs)
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = str(msg)
        for i in args:
            msg += ', ' + str(i)
        args = []
        msg, kwargs = self.process(msg, kwargs)
        self.logger.info(msg, *args, **kwargs)

    def print(self, msg, *args, **kwargs):
        # Hacky piece of code to report both the names and the values of variables passed to info.
        frame = inspect.currentframe()
        frame = inspect.getouterframes(frame)[1]
        string = inspect.getframeinfo(frame[0]).code_context[0].strip()
        names = string[string.find('(') + 1:-1].split(',')
        names = [i.replace(' ', '') for i in names]

        if type(msg) is not str:
            msg = '\n' + names[0] + ':\t' + str(msg)
        else:
            msg = '\n' + msg
        for c, i in enumerate(args):
            # print('names', names, c, i)
            if type(i) is not str:
                msg += '\n' + str(names[c + 1]) + ':\t' + str(i)
            else:
                msg += '\n' + str(i)

        msg = msg.expandtabs(30)

        args = []
        msg, kwargs = self.process(msg, kwargs)

        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        for i in args:
            msg += ', ' + str(i)
        msg, kwargs = self.process(msg, kwargs)
        stack_list = traceback.format_stack()

        key_file_root = hb.file_root(sys.argv[0])

        key_stack_elements = ''
        rest_of_stack = ''
        for i in range(len(stack_list)):
            if key_file_root in stack_list[i]:
                key_stack_elements += stack_list[i].split(', in ')[0]
            rest_of_stack += ' ' + str(stack_list[i].split(', in ')[0])

        if key_stack_elements:
            msg = str(msg) + ' ' + key_stack_elements + '. Rest of stack trace: '+ rest_of_stack
        else:
            msg = str(msg) + ' Stack trace: ' + rest_of_stack
        msg = 'WARNING ' + msg
        self.logger.warning(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        for i in args:
            msg += ', ' + str(i)
        msg, kwargs = self.process(msg, kwargs)
        stack_list = traceback.format_stack()
        warning_string = ''
        # stack_list.reverse()
        for i in range(len(stack_list)):
            warning_string += ' ' + stack_list[i].split(', in ')[0] + '\n'
        msg = str(msg) + ' Stacktrace:\n' + warning_string
        msg = 'CRITICAL ' + msg
        self.logger.critical(msg, *args, **kwargs)

    def set_log_file_uri(self, uri):
        hdlr = logging.FileHandler(uri)
        self.logger.addHandler(hdlr)



FORMAT = "%(message)s              --- %(asctime)s --- %(name)s %(levelname)s"
# FORMAT = "%(message)s"
logging.basicConfig(format=FORMAT)

LOGGING_LEVEL = logging.INFO

L = logging.getLogger('hazelbean')

L.setLevel(LOGGING_LEVEL)
L.addHandler(logging.NullHandler())  # silence logging by default

L = CustomLogger(L, {'msg': 'Custom message: '})

logging_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'critical': logging.CRITICAL,
}

##Deactvated logging to file.
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)#
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
# L.addHandler(handler)
# logging.Logger.debug_deeper_1 = debug_deeper_1

def get_logger(logger_name=None, logging_level='info', format='full'):
    """Used to get a custom logger specific to a file other than just susing the config defined one."""
    if not logger_name:
        try:
            logger_name = os.path.basename(main.__file__)
        except:
            logger_name = 'unnamed_logger'
    L = logging.getLogger(logger_name)
    L.setLevel(logging_levels[logging_level])
    CL = CustomLogger(L, {'msg': 'Custom message: '})
    # FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    FORMAT = "%(message)s"
    formatter = logging.Formatter(FORMAT)

    # handler = logging.StreamHandler()
    # handler.setFormatter(formatter)
    # L.addHandler(handler)
    return CL

def critical(self, msg, *args, **kwargs):
    """
    Delegate a debug call to the underlying logger, after adding
    contextual information from this adapter instance.
    """
    msg, kwargs = self.process_critical_logger(msg, kwargs)
    L.critical(msg, *args, **kwargs)

if not os.path.exists(TEMPORARY_DIR):
    try:
        os.makedirs(TEMPORARY_DIR)
    except:
        raise Exception('Could not create temp file at ' + TEMPORARY_DIR + '. Perhaps you do not have permission? Try setting hazelbean/config.TEMPORARY_DIR to something in your user folder.')

uris_to_delete_at_exit = []
plots_to_display_at_exit = []


def general_callback(df_complete, psz_message, p_progress_arg):
    """The argument names come from the GDAL API for callbacks."""
    try:
        current_time = time.time()
        if ((current_time - general_callback.last_time) > 5.0 or
                (df_complete == 1.0 and general_callback.total_time >= 5.0)):
            print(
                "ReprojectImage %.1f%% complete %s, psz_message %s",
                df_complete * 100, p_progress_arg[0], psz_message)
            general_callback.last_time = current_time
            general_callback.total_time += current_time
    except AttributeError:
        general_callback.last_time = time.time()
        general_callback.total_time = 0.0

# -- GLOBAL CONSTANTS
start_of_numerals_ascii_int = 48
start_of_uppercase_letters_ascii_int = 65
start_of_lowercase_letters_ascii_int = 97
alphanumeric_ascii_ints = list(range(start_of_numerals_ascii_int, start_of_numerals_ascii_int + 10)) + list(range(start_of_uppercase_letters_ascii_int, start_of_uppercase_letters_ascii_int + 26)) + list(range(start_of_lowercase_letters_ascii_int, start_of_lowercase_letters_ascii_int + 26))
alphanumeric_lowercase_ascii_ints = list(range(start_of_numerals_ascii_int, start_of_numerals_ascii_int + 10)) + list(range(start_of_lowercase_letters_ascii_int, start_of_lowercase_letters_ascii_int + 26))
alphanumeric_ascii_symbols = [chr(i) for i in alphanumeric_ascii_ints]
alphanumeric_lowercase_ascii_symbols = [chr(i) for i in alphanumeric_lowercase_ascii_ints] # numbers are lowercase i assume...


def delete_path_at_exit(path):
    if not os.path.exists(path):
        raise NameError('Cannot delete path ' + path + ' that does not exist.')
    if path in uris_to_delete_at_exit:
        L.warning('Attempted to add ' + path + ' to uris_to_delete_at_exit but it was already in there.')
        return
    else:
        uris_to_delete_at_exit.append(path)

def gdal_to_numpy_type(band):
    return _gdal_to_numpy_type(band)

def _gdal_to_numpy_type(band):
    """Calculate the equivalent numpy datatype from a GDAL raster band type.

    Args:
        band (gdal.Band): GDAL band

    Returns:
        numpy_datatype (numpy.dtype): equivalent of band.DataType
    """

    gdal_type_to_numpy_lookup = {
        gdal.GDT_Int16: numpy.int16,
        gdal.GDT_Int32: numpy.int32,
        gdal.GDT_UInt16: numpy.uint16,
        gdal.GDT_UInt32: numpy.uint32,
        gdal.GDT_Float32: numpy.float32,
        gdal.GDT_Float64: numpy.float64
    }

    if band.DataType in gdal_type_to_numpy_lookup:
        return gdal_type_to_numpy_lookup[band.DataType]

    # only class not in the lookup is a Byte but double check.
    if band.DataType != gdal.GDT_Byte:
        raise ValueError("Unknown DataType: %s" % str(band.DataType))

    metadata = band.GetMetadata('IMAGE_STRUCTURE')
    if 'PIXELTYPE' in metadata and metadata['PIXELTYPE'] == 'SIGNEDBYTE':
        return numpy.int8
    return numpy.uint8



# I got confused on  the foloowing two  lists. See http://www.gdal.org/ogr__core_8h.html#a787194bea637faf12d61643124a7c9fc
gdal_number_to_ogr_field_type = {
    1: 0, # not sure if not OFSTBoolean
    2: 0, # seemed to be unimplemented as uint etc.
    3: 0,
    4: 0,
    5: 0,
    6: 2,
    7: 2, # not sure if correct
}

type_string_to_ogr_field_type = {
    'int': gdal_number_to_ogr_field_type[1],
    'uint': gdal_number_to_ogr_field_type[1],
    'uint8': gdal_number_to_ogr_field_type[1],
    'uint16': gdal_number_to_ogr_field_type[1],
    'int16': gdal_number_to_ogr_field_type[1],
    'uint32': gdal_number_to_ogr_field_type[1],
    'int32': gdal_number_to_ogr_field_type[1],
    'float': gdal_number_to_ogr_field_type[6],
    'float32': gdal_number_to_ogr_field_type[6],
    'float64': gdal_number_to_ogr_field_type[7],
    'string': 4,
}

gdal_number_to_gdal_type = {
    1: gdalconst.GDT_Byte,
    2: gdalconst.GDT_UInt16,
    3: gdalconst.GDT_Int16,
    4: gdalconst.GDT_UInt32,
    5: gdalconst.GDT_Int32,
    6: gdalconst.GDT_Float32,
    7: gdalconst.GDT_Float64,
    8: gdalconst.GDT_CInt16,
    9: gdalconst.GDT_CInt32,
    10: gdalconst.GDT_CFloat32,
    11: gdalconst.GDT_CFloat64,
}

gdal_number_to_gdal_name = {
    1: 'Byte',
    2: 'UInt16',
    3: 'Int16',
    4: 'UInt32',
    5: 'Int32',
    6: 'Float32',
    7: 'Float64',
    8: 'CInt16',
    9: 'CInt32',
    10: 'CFloat32',
    11: 'CFloat64'
}

gdal_name_to_gdal_number = {
    'Byte': 1,
    'uint8': 1,
    'Uint8': 1,
    'UInt16': 2,
    'Int16': 3,
    'UInt32': 4,
    'Int32': 5,
    'Float32': 6,
    'Float64': 7,
    'CInt16': 8,
    'CInt32': 9,
    'CFloat32': 10,
    'CFloat64': 11,
    'byte': 1,
    'uint16': 2,
    'int16': 3,
    'uint32': 4,
    'int32': 5,
    'float32': 6,
    'float64': 7,
    'cint16': 8,
    'cint32': 9,
    'cfloat32': 10,
    'cfloat64': 11,
}

gdal_number_to_numpy_type = {
    1: numpy.uint8,
    2: numpy.uint16,
    3: numpy.int16,
    4: numpy.uint32,
    5: numpy.int32,
    6: numpy.float32,
    7: numpy.float64,
    8: numpy.complex64,
    9: numpy.complex64,
    10: numpy.complex64,
    11: numpy.complex128
}

numpy_type_to_gdal_number = {
    numpy.uint8: 1,
    numpy.uint16: 2,
    numpy.int16: 3,
    numpy.uint32: 4,
    numpy.int32: 5,
    numpy.float32: 6,
    numpy.float64: 7,
    numpy.complex64: 8,  # THe omission here is from the unexplained duplication in gdal_number_to_numpy_type
    numpy.complex128: 11,
    numpy.int64: 7, # NOTE, gdal does not support 64bit ints.

    np.dtype('uint8'): 1,
    np.dtype('uint16'): 2,
    np.dtype('int16'): 3,
    np.dtype('uint32'): 4,
    np.dtype('int32'): 5,
    np.dtype('float32'): 6,
    np.dtype('float64'): 7,
    np.dtype('complex64'): 8,  # THe omission here is from the unexplained duplication in gdal_number_to_numpy_type
    np.dtype('complex128'): 11,
    np.dtype('int64'): 7,

}

numpy_name_to_gdal_number = {
    'int8': 1,
    'uint8': 1,
    'uint16': 2,
    'int16': 3,
    'uint32': 4,
    'int32': 5,
    'int64': 7, # WTF couldnt find gdal's int64 type . might not exist?
    'uint64': 7, # WTF couldnt find gdal's int64 type . might not exist?
    'float32': 6,
    'float64': 7,
    'complex64': 8,  # THe omission here is from the unexplained duplication in gdal_number_to_numpy_type
    'complex128': 11,
}

gdal_type_to_numpy_type = {
    gdalconst.GDT_Byte: numpy.uint8,
    gdalconst.GDT_UInt16: numpy.uint16,
    gdalconst.GDT_Int16: numpy.int16,
    gdalconst.GDT_UInt32: numpy.uint32,
    gdalconst.GDT_Int32: numpy.int32,
    gdalconst.GDT_Float32: numpy.float32,
    gdalconst.GDT_Float64: numpy.float64,
    gdalconst.GDT_CInt16: numpy.complex64,
    gdalconst.GDT_CInt32: numpy.complex64,
    gdalconst.GDT_CFloat32: numpy.complex64,
    gdalconst.GDT_CFloat64: numpy.complex128
}

GDAL_TO_NUMPY_TYPE = {
    gdal.GDT_Byte: numpy.uint8,
    gdal.GDT_Int16: numpy.int16,
    gdal.GDT_Int32: numpy.int32,
    gdal.GDT_UInt16: numpy.uint16,
    gdal.GDT_UInt32: numpy.uint32,
    gdal.GDT_Float32: numpy.float32,
    gdal.GDT_Float64: numpy.float64
}

numpy_type_to_gdal_type = {
    numpy.uint8: gdalconst.GDT_Byte,
    numpy.uint16: gdalconst.GDT_UInt16,
    numpy.int16: gdalconst.GDT_Int16,
    numpy.uint32: gdalconst.GDT_UInt32,
    numpy.int32: gdalconst.GDT_Int32,
    numpy.float32: gdalconst.GDT_Float32,
    numpy.float64: gdalconst.GDT_Float64,
    numpy.complex64: gdalconst.GDT_CInt16,
    numpy.complex64: gdalconst.GDT_CInt32,
    numpy.complex64: gdalconst.GDT_CFloat32,
    numpy.complex128: gdalconst.GDT_CFloat64,
    np.int64: gdalconst.GDT_Float64
}


common_epsg_codes_by_name = OrderedDict()
common_epsg_codes_by_name['wgs84'] =  4326
common_epsg_codes_by_name['wec'] =  54002
common_epsg_codes_by_name['world_eckert_iv'] =  54012
common_epsg_codes_by_name['robinson'] =  54030
# common_epsg_codes_by_name['mollweide'] =  54009
common_epsg_codes_by_name['plate_carree'] =  32662
# common_epsg_codes_by_name['mercator'] =  3857
# common_epsg_codes_by_name[]# '] = wec_old': 32663,
# common_epsg_codes_by_name[]# '] = wec_sphere': 3786,

common_projected_epsg_codes_by_name = OrderedDict()
# common_projected_epsg_codes_by_name['wgs84'] =  4326
common_projected_epsg_codes_by_name['wec'] =  54002
common_projected_epsg_codes_by_name['world_eckert_iv'] =  54012
common_projected_epsg_codes_by_name['robinson'] =  54030
# common_projected_epsg_codes_by_name['mollweide'] =  54009
common_projected_epsg_codes_by_name['plate_carree'] =  32662
# common_projected_epsg_codes_by_name['mercator'] =  3857

# Based on WGS84 (G1762)'
wgs_84_wkt = """GEOGCS["WGS 84", DATUM["WGS_1984", SPHEROID["WGS 84", 6378137, 298.257223563, AUTHORITY["EPSG", "7030"]], AUTHORITY["EPSG", "6326"]], PRIMEM["Greenwich", 0, AUTHORITY["EPSG", "8901"]], UNIT["degree", 0.0174532925199433, AUTHORITY["EPSG", "9122"]], AUTHORITY["EPSG", "4326"]]"""
mollweide_wkt = """PROJCS["World_Mollweide", GEOGCS["GCS_WGS_1984", DATUM["WGS_1984", SPHEROID["WGS_1984", 6378137, 298.257223563]], PRIMEM["Greenwich", 0], UNIT["Degree", 0.017453292519943295]], PROJECTION["Mollweide"], PARAMETER["False_Easting", 0], PARAMETER["False_Northing", 0], PARAMETER["Central_Meridian", 0], UNIT["Meter", 1], AUTHORITY["EPSG", "54009"]]"""

robinson_wkt = """PROJCS["World_Robinson",
    GEOGCS["GCS_WGS_1984",
        DATUM["WGS_1984",
            SPHEROID["WGS_1984",6378137,298.257223563]],
        PRIMEM["Greenwich",0],
        UNIT["Degree",0.017453292519943295]],
    PROJECTION["Robinson"],
    PARAMETER["False_Easting",0],
    PARAMETER["False_Northing",0],
    PARAMETER["Central_Meridian",0],
    UNIT["Meter",1],
    AUTHORITY["EPSG","54030"]]"""

wgs_84_wkt = """GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.01745329251994328,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]"""

cylindrical_wkt = """PROJCS["WGS 84 / World Equidistant Cylindrical",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.01745329251994328,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"],
        AXIS["Latitude",NORTH],
        AXIS["Longitude",EAST]],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]]]"""

plate_carree_wkt = """PROJCS["WGS 84 / Plate Carree (deprecated)",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.01745329251994328,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    PROJECTION["Equirectangular"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",0],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    AUTHORITY["EPSG","32662"],
    AXIS["X",EAST],
    AXIS["Y",NORTH]]"""




# Not used in WGS84 standard
more_precise_degree_measurement = 0.01745329251994328

common_geotransforms = {
    'global_5m': (-180.0, 0.08333333333333333, 0.0, 90.0, 0.0, -0.08333333333333333), # NOTE, the 0.08333333333333333 is defined very precisely as the answer a 64 bit compiled python gives from the answer 1/12 (i.e. 5 arc minutes)
    'global_30s': (-180.0, 0.008333333333333333, 0.0, 90.0, 0.0, -0.008333333333333333),  # NOTE, the 0.008333333333333333 is defined very precisely as the answer a 64 bit compiled python gives from the answer 1/120 (i.e. 30 arc seconds) Note that this has 1 more digit than 1/12 due to how floating points are stored in computers via exponents.
}

geotransform_global_4deg = (-180.0, 2, 0.0, 90.0, 0.0, -4)
geotransform_global_2deg = (-180.0, 2, 0.0, 90.0, 0.0, -2)
geotransform_global_1deg = (-180.0, 1, 0.0, 90.0, 0.0, -1)
geotransform_global_30m = (-180.0, 0.5, 0.0, 90.0, 0.0, -0.5)
geotransform_global_15m = (-180.0, 0.25, 0.0, 90.0, 0.0, -0.25)
geotransform_global_5m = (-180.0, 0.08333333333333333, 0.0, 90.0, 0.0, -0.08333333333333333)  # NOTE, the 0.08333333333333333 is defined very precisely as the answer a 64 bit compiled python gives from the answer 1/12 (i.e. 5 arc minutes)
geotransform_global_30s = (-180.0, 0.008333333333333333, 0.0, 90.0, 0.0, -0.008333333333333333)  # NOTE, the 0.008333333333333333 is defined very precisely as the answer a 64 bit compiled python gives from the answer 1/120 (i.e. 30 arc seconds) Note that this has 1 more digit than 1/12 due to how floating points are stored in computers via exponents.
geotransform_global_10s = (-180.0, 0.002777777777777778, 0.0, 90.0, 0.0, -0.002777777777777778)  # NOTE, the 0.002777777777777778 is defined very precisely


def get_global_geotransform_from_resolution(input_resolution):
    return (-180.0, input_resolution, 0.0, 90.0, 0.0, -input_resolution)

common_bounding_boxes_in_degrees = {
    'global': [-180., -90., 180., 90.]
}

common_projection_wkts = {
    'wgs84': "GEOGCS[\"WGS 84\", DATUM[\"WGS_1984\", SPHEROID[\"WGS 84\", 6378137, 298.257223563, AUTHORITY[\"EPSG\", \"7030\"]], AUTHORITY[\"EPSG\", \"6326\"]],PRIMEM[\"Greenwich\", 0], UNIT[\"degree\", 0.0174532925199433], AUTHORITY[\"EPSG\", \"4326\"]]"
}

default_no_data_values_by_gdal_number = {
    1: 255,
    2: 65535,
    3: -32768,
    4: 0, # NOTE MASSIVE FLAW, because QGIS/GDAL doesnt support UInt32, had to clamp it to 0
    # 5: -2147483647,
    5: -2147483648,
    6: -9999.0,
    7: -9999.0,
}

default_no_data_values_by_gdal_number_in_numpy_types = {
    1: np.float(255),
    2: np.float(65535),
    3: np.float(-32768),
    4: np.float(0), # NOTE MASSIVE FLAW, because QGIS/GDAL doesnt support UInt32, had to clamp it to 0
    # 5: -2147483647,
    5: np.float(-2147483648),
    6: np.float(-9999.0),
    7: np.float(-9999.0),
}

default_no_data_values_by_gdal_stringed_number = {
    '1': 255,
    '2': 65535,
    '3': -32768,
    '4': 0, # NOTE MASSIVE FLAW, because QGIS/GDAL doesnt support UInt32, had to clamp it to 0
    # '5': -2147483647,
    '5': -2147483648,
    '6': -9999.0,
    '7': -9999.0,
    ## The following didn't work beacuse they couldn't  be written via Band.SetNoDataValue() in gdal.
    # '6': -3.4028235e+38,
    # '7': -1.7976931348623157e+308
    # '6': float(np.finfo(np.float32).min),
    # '7': float(np.finfo(np.float64).min),
}

default_no_data_values_by_numpy_type = {
    np.uint8: 255,
    np.byte: 255,
    np.uint16: 65535,
    np.int16: -32768,
    np.uint32: 0,  # NOTE MASSIVE FLAW, because QGIS/GDAL doesnt support UInt32, had to clamp it to 0
    np.int: -2147483648,
    np.int32: -2147483648,
    np.float32: -9999.0,
    np.float: -9999.0,
    np.float64: -9999.0,
}


default_no_data_values_by_numpy_type_and_as_numpy_types = {
    np.uint8: np.uint8(255),
    np.byte: np.byte(255),
    np.uint16: np.uint16(65535),
    np.int16: np.int16(-32768),
    np.uint32: np.uint32(0),  # NOTE MASSIVE FLAW, because QGIS/GDAL doesnt support UInt32, had to clamp it to )0
    np.int: np.int(-2147483648),
    np.int32: np.int32(-2147483648),
    np.float32: np.float32(-9999.0),
    np.float: np.float(-9999.0),
    np.float64: np.float64(-9999.0),
}


size_of_one_arcdegree_at_equator_in_meters = 111319.49079327358  # Based on (2 * math.pi * 6378.137*1000) / 360  # old 111319



esacci_standard_classes = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, ]

esacci_standard_class_descriptions = OrderedDict()
esacci_standard_class_descriptions[0] = 'No Data'
esacci_standard_class_descriptions[10] = 'Cropland, rainfed'
esacci_standard_class_descriptions[20] = 'Cropland, irrigated or post-flooding'
esacci_standard_class_descriptions[30] = 'Mosaic cropland (>50%) / natural vegetation (tree, shrub, herbaceous cover)(<50%)'
esacci_standard_class_descriptions[40] = 'Mosaic natural vegetation (tree, shrub, herbaceous cover) (>50%) / cropland(<50%)'
esacci_standard_class_descriptions[50] = 'Tree cover, broadleaved, evergreen, closed to open (>15%)'
esacci_standard_class_descriptions[60] = 'Tree cover, broadleaved, deciduous, closed to open (>15%)'
esacci_standard_class_descriptions[70] = 'Tree cover, needleleaved, evergreen, closed to open (>15%)'
esacci_standard_class_descriptions[80] = 'Tree cover, needleleaved, deciduous, closed to open (>15%)'
esacci_standard_class_descriptions[90] = 'Tree cover, mixed leaf type (broadleaved and needleleaved)'
esacci_standard_class_descriptions[100] = 'Mosaic tree and shrub (>50%) / herbaceous cover (<50%)'
esacci_standard_class_descriptions[110] = 'Mosaic herbaceous cover (>50%) / tree and shrub (<50%)'
esacci_standard_class_descriptions[120] = 'Shrubland'
esacci_standard_class_descriptions[130] = 'Grassland'
esacci_standard_class_descriptions[140] = 'Lichens and mosses'
esacci_standard_class_descriptions[150] = 'Sparse vegetation (tree, shrub, herbaceous cover) (<15%)'
esacci_standard_class_descriptions[160] = 'Tree cover, flooded, fresh or brakish water'
esacci_standard_class_descriptions[170] = 'Tree cover, flooded, saline water'
esacci_standard_class_descriptions[180] = 'Shrub or herbaceous cover, flooded, fresh/saline/brakish water' # Underestimates wetland GIEMS might be able to improve this (lehner et al.)
esacci_standard_class_descriptions[190] = 'Urban areas'
esacci_standard_class_descriptions[200] = 'Bare areas'
esacci_standard_class_descriptions[210] = 'Water bodies'
esacci_standard_class_descriptions[220] = 'Permanent snow and ice'

esacci_extended_classes = [0, 10, 11, 12, 20, 30, 40, 50, 60, 61, 62, 70, 71, 72, 80, 81, 82, 90, 100, 110, 120, 121, 122, 130, 140, 150, 151, 152, 153, 160, 170, 180, 190, 200, 201, 202, 210, 220]
esacci_extended_class_descriptions = OrderedDict()
esacci_extended_class_descriptions[0] = 'No Data'
esacci_extended_class_descriptions[10] = 'Cropland, rainfed'
esacci_extended_class_descriptions[11] = 'Cropland, rainfed, herbaceous cover'
esacci_extended_class_descriptions[12] = 'Cropland, rainfed, tree or shrub cover'
esacci_extended_class_descriptions[20] = 'Cropland, irrigated or post-flooding'
esacci_extended_class_descriptions[30] = 'Mosaic cropland (>50%) / natural vegetation (tree, shrub, herbaceous cover)(<50%)'
esacci_extended_class_descriptions[40] = 'Mosaic natural vegetation (tree, shrub, herbaceous cover) (>50%) / cropland(<50%)'
esacci_extended_class_descriptions[50] = 'Tree cover, broadleaved, evergreen, closed to open (>15%)'
esacci_extended_class_descriptions[60] = 'Tree cover, broadleaved, deciduous, closed to open (>15%)'
esacci_extended_class_descriptions[61] = 'Tree cover, broadleaved, deciduous, closed (>40%)'
esacci_extended_class_descriptions[62] = 'Tree cover, broadleaved, deciduous, open (15-40%)'
esacci_extended_class_descriptions[70] = 'Tree cover, needleleaved, evergreen, closed to open (>15%)'
esacci_extended_class_descriptions[71] = 'Tree cover, needleleaved, evergreen, closed to open (>15%)'
esacci_extended_class_descriptions[72] = 'Tree cover, needleleaved, evergreen, open (15-40%)'
esacci_extended_class_descriptions[80] = 'Tree cover, needleleaved, deciduous, closed to open (>15%)'
esacci_extended_class_descriptions[81] = 'Tree cover, needleleaved, deciduous, closed (>40%)'
esacci_extended_class_descriptions[82] = 'Tree cover, needleleaved, deciduous, open (15-40%)'
esacci_extended_class_descriptions[90] = 'Tree cover, mixed leaf type (broadleaved and needleleaved)'
esacci_extended_class_descriptions[100] = 'Mosaic tree and shrub (>50%) / herbaceous cover (<50%)'
esacci_extended_class_descriptions[110] = 'Mosaic herbaceous cover (>50%) / tree and shrub (<50%)'
esacci_extended_class_descriptions[120] = 'Shrubland'
esacci_extended_class_descriptions[121] = 'Evergreen shrubland'
esacci_extended_class_descriptions[122] = 'Deciduous shrubland '
esacci_extended_class_descriptions[130] = 'Grassland'
esacci_extended_class_descriptions[140] = 'Lichens and mosses'
esacci_extended_class_descriptions[150] = 'Sparse vegetation (tree, shrub, herbaceous cover) (<15%)'
esacci_extended_class_descriptions[151] = 'Sparse tree (<15%)'
esacci_extended_class_descriptions[152] = 'Sparse shrub (<15%)'
esacci_extended_class_descriptions[153] = 'Sparse herbaceous cover (<15%)'
esacci_extended_class_descriptions[160] = 'Tree cover, flooded, fresh or brakish water'
esacci_extended_class_descriptions[170] = 'Tree cover, flooded, saline water'
esacci_extended_class_descriptions[180] = 'Shrub or herbaceous cover, flooded, fresh/saline/brakish water'
esacci_extended_class_descriptions[190] = 'Urban areas'
esacci_extended_class_descriptions[200] = 'Bare areas'
esacci_extended_class_descriptions[201] = 'Consolidated bare areas'
esacci_extended_class_descriptions[202] = 'Unconsolidated bare areas'
esacci_extended_class_descriptions[210] = 'Water bodies'
esacci_extended_class_descriptions[220] = 'Permanent snow and ice'






esacci_extended_short_class_descriptions = OrderedDict()
esacci_extended_short_class_descriptions[0] = 'ndv'
esacci_extended_short_class_descriptions[10] = 'crop_rainfed'
esacci_extended_short_class_descriptions[11] = 'crop_rainfed_herb'
esacci_extended_short_class_descriptions[12] = 'crop_rainfed_tree'
esacci_extended_short_class_descriptions[20] = 'crop_irrigated'
esacci_extended_short_class_descriptions[30] = 'crop_natural_mosaic'
esacci_extended_short_class_descriptions[40] = 'natural_crop_mosaic'
esacci_extended_short_class_descriptions[50] = 'tree_broadleaved_evergreen'
esacci_extended_short_class_descriptions[60] = 'tree_broadleaved_deciduous_closed_to_open_15'
esacci_extended_short_class_descriptions[61] = 'tree_broadleaved_deciduous_closed_40'
esacci_extended_short_class_descriptions[62] = 'tree_broadleaved_deciduous_open_15_40'
esacci_extended_short_class_descriptions[70] = 'tree_needleleaved_evergreen_closed_to_open_15'
esacci_extended_short_class_descriptions[71] = 'tree_needleleaved_evergreen_closed_to_open_15_extended'
esacci_extended_short_class_descriptions[72] = 'tree_needleleaved_evergreen_open_15_40'
esacci_extended_short_class_descriptions[80] = 'tree_needleleaved_deciduous_closed_to_open_15'
esacci_extended_short_class_descriptions[81] = 'tree_needleleaved_deciduous_closed_40'
esacci_extended_short_class_descriptions[82] = 'tree_needleleaved_deciduous_open_15_40'
esacci_extended_short_class_descriptions[90] = 'tree_mixed_type'
esacci_extended_short_class_descriptions[100] = 'mosaic_tree_and_shrub_50_herbaceous_cover_50'
esacci_extended_short_class_descriptions[110] = 'mosaic_herbaceous_cover_50_tree_and_shrub_50'
esacci_extended_short_class_descriptions[120] = 'shrubland'
esacci_extended_short_class_descriptions[121] = 'evergreen_shrubland'
esacci_extended_short_class_descriptions[122] = 'deciduous_shrubland'
esacci_extended_short_class_descriptions[130] = 'grassland'
esacci_extended_short_class_descriptions[140] = 'lichens_and_mosses'
esacci_extended_short_class_descriptions[150] = 'sparse_vegetation_tree_shrub_herbaceous_cover_15'
esacci_extended_short_class_descriptions[151] = 'sparse_tree_15'
esacci_extended_short_class_descriptions[152] = 'sparse_shrub_15'
esacci_extended_short_class_descriptions[153] = 'sparse_herbaceous_cover_15'
esacci_extended_short_class_descriptions[160] = 'tree_cover_flooded_fresh_or_brakish_water'
esacci_extended_short_class_descriptions[170] = 'tree_cover_flooded_saline_water'
esacci_extended_short_class_descriptions[180] = 'shrub_or_herbaceous_cover_flooded_fresh_saline_brakish_water'
esacci_extended_short_class_descriptions[190] = 'urban_areas'
esacci_extended_short_class_descriptions[200] = 'bare_areas'
esacci_extended_short_class_descriptions[201] = 'consolidated_bare_areas'
esacci_extended_short_class_descriptions[202] = 'unconsolidated_bare_areas'
esacci_extended_short_class_descriptions[210] = 'water_bodies'
esacci_extended_short_class_descriptions[220] = 'permanent_snow_and_ice'

# Decided this is the preferred method for storing the correspondence data and then also making it into a rules dict.
esacci_to_seals_simplified_correspondence = OrderedDict()
esacci_to_seals_simplified_correspondence[0] = [0, 'ndv', 'ndv']
esacci_to_seals_simplified_correspondence[10] = [2, 'crop_rainfed', 'crop']
esacci_to_seals_simplified_correspondence[11] = [2, 'crop_rainfed_herb', 'crop']
esacci_to_seals_simplified_correspondence[12] = [2, 'crop_rainfed_tree', 'crop']
esacci_to_seals_simplified_correspondence[20] = [2, 'crop_irrigated', 'crop']
esacci_to_seals_simplified_correspondence[30] = [2, 'crop_natural_mosaic', 'crop']
esacci_to_seals_simplified_correspondence[40] = [2, 'natural_crop_mosaic', 'crop']
esacci_to_seals_simplified_correspondence[50] = [4, 'tree_broadleaved_evergreen', 'forest']
esacci_to_seals_simplified_correspondence[60] = [4, 'tree_broadleaved_deciduous_closed_to_open_15', 'forest']
esacci_to_seals_simplified_correspondence[61] = [4, 'tree_broadleaved_deciduous_closed_40', 'forest']
esacci_to_seals_simplified_correspondence[62] = [4, 'tree_broadleaved_deciduous_open_15_40', 'forest']
esacci_to_seals_simplified_correspondence[70] = [4, 'tree_needleleaved_deciduous_closed_to_open_15', 'forest']
esacci_to_seals_simplified_correspondence[71] = [4, 'tree_needleleaved_evergreen_closed_to_open_15_extended', 'forest']
esacci_to_seals_simplified_correspondence[72] = [4, 'tree_needleleaved_evergreen_open_15_40', 'forest']
esacci_to_seals_simplified_correspondence[80] = [4, 'tree_needleleaved_deciduous_closed_to_open_15', 'forest']
esacci_to_seals_simplified_correspondence[81] = [4, 'tree_needleleaved_deciduous_closed_40', 'forest']
esacci_to_seals_simplified_correspondence[82] = [4, 'tree_needleleaved_deciduous_open_15_40', 'forest']
esacci_to_seals_simplified_correspondence[90] = [4, 'tree_mixed_type', 'forest']
esacci_to_seals_simplified_correspondence[100] = [4, 'mosaic_tree_and_shrub_50_herbaceous_cover_50', 'forest']
esacci_to_seals_simplified_correspondence[110] = [5, 'mosaic_herbaceous_cover_50_tree_and_shrub_50', 'shrubland']
esacci_to_seals_simplified_correspondence[120] = [5, 'shrubland', 'shrubland']
esacci_to_seals_simplified_correspondence[121] = [5, 'evergreen_shrubland', 'shrubland']
esacci_to_seals_simplified_correspondence[122] = [5, 'deciduous_shrubland', 'shrubland']
esacci_to_seals_simplified_correspondence[130] = [3, 'grassland', 'grassland']
esacci_to_seals_simplified_correspondence[140] = [5, 'lichens_and_mosses', 'shrubland']
esacci_to_seals_simplified_correspondence[150] = [5, 'sparse_vegetation_tree_shrub_herbaceous_cover_15', 'shrubland']
esacci_to_seals_simplified_correspondence[151] = [4, 'sparse_tree_15', 'forest']
esacci_to_seals_simplified_correspondence[152] = [5, 'sparse_shrub_15', 'shrubland']
esacci_to_seals_simplified_correspondence[153] = [5, 'sparse_herbaceous_cover_15', 'shrubland']
esacci_to_seals_simplified_correspondence[160] = [4, 'tree_cover_flooded_fresh_or_brakish_water', 'forest']
esacci_to_seals_simplified_correspondence[170] = [4, 'tree_cover_flooded_saline_water', 'forest']
esacci_to_seals_simplified_correspondence[180] = [5, 'shrub_or_herbaceous_cover_flooded_fresh_saline_brakish_water', 'shrubland']
esacci_to_seals_simplified_correspondence[190] = [1, 'urban_areas', 'urban']
esacci_to_seals_simplified_correspondence[200] = [7, 'bare_areas', 'other']
esacci_to_seals_simplified_correspondence[201] = [7, 'consolidated_bare_areas', 'other']
esacci_to_seals_simplified_correspondence[202] = [7, 'unconsolidated_bare_areas', 'other']
esacci_to_seals_simplified_correspondence[210] = [6, 'water_bodies', 'water']
esacci_to_seals_simplified_correspondence[220] = [7, 'permanent_snow_and_ice', 'other']

# Decided this is the preferred method for storing the correspondence data and then also making it into a rules dict.
esacci_to_seals_simplified_rules = OrderedDict(zip(esacci_to_seals_simplified_correspondence.keys(), [i[0] for i in esacci_to_seals_simplified_correspondence.values()]))

seals_simplified_to_esacci_correspondence = OrderedDict()
seals_simplified_to_esacci_correspondence[0] = [0, 'ndv', 'ndv']
seals_simplified_to_esacci_correspondence[1] = [190, 'urban', 'urban_areas']
seals_simplified_to_esacci_correspondence[2] = [10, 'crop', 'crop_rainfed']
seals_simplified_to_esacci_correspondence[3] = [130, 'grassland', 'grassland']
seals_simplified_to_esacci_correspondence[4] = [50, 'forest', 'tree_broadleaved_evergreen']
seals_simplified_to_esacci_correspondence[5] = [120, 'shrubland', 'shrubland']
seals_simplified_to_esacci_correspondence[6] = [210, 'water', 'water_bodies']
seals_simplified_to_esacci_correspondence[7] = [200,  'other', 'bare_areas']

# Decided this is the preferred method for storing the correspondence data and then also making it into a rules dict.
seals_simplified_to_esa_rules = OrderedDict(zip(seals_simplified_to_esacci_correspondence.keys(), [i[0] for i in seals_simplified_to_esacci_correspondence.values()]))

glc_classes_to_labels = OrderedDict()
glc_classes_to_labels[1] = 'tree_broadleaved_evergreen'
glc_classes_to_labels[2] = 'tree_broadleaved_deciduous_closed'
glc_classes_to_labels[3] = 'tree_broadleaved_deciduous_open'
glc_classes_to_labels[4] = 'tree_needleleaved_evergreen'
glc_classes_to_labels[5] = 'tree_needleleaved_deciduous'
glc_classes_to_labels[6] = 'tree_mixed_type'
glc_classes_to_labels[7] = 'tree_cover_flooded_fresh_or_brakish_water'
glc_classes_to_labels[8] = 'tree_cover_flooded_saline_water'
glc_classes_to_labels[9] = 'mosaic'
glc_classes_to_labels[10] = 'tree_cover_burnt'
glc_classes_to_labels[11] = 'evergreen_shrubland'
glc_classes_to_labels[12] = 'deciduous_shrubland'
glc_classes_to_labels[13] = 'herbaceous'
glc_classes_to_labels[14] = 'sparse_herbaceous_cover'
glc_classes_to_labels[15] = 'shrub_or_herbaceous_cover_flooded_fresh_saline_brakish_water'
glc_classes_to_labels[16] = 'cultivated'
glc_classes_to_labels[17] = 'crop_tree_mosaic'
glc_classes_to_labels[18] = 'crop_shrub_mosaic'
glc_classes_to_labels[19] = 'bare'
glc_classes_to_labels[20] = 'water'
glc_classes_to_labels[21] = 'snow_and_ice'
glc_classes_to_labels[22] = 'artificial_surface'


esacci_to_glc2000_correspondence = OrderedDict()
esacci_to_glc2000_correspondence[0] = [0, 'ndv']
esacci_to_glc2000_correspondence[10] = [16, 'crop_rainfed']
esacci_to_glc2000_correspondence[11] = [16, 'crop_rainfed_herb']
esacci_to_glc2000_correspondence[12] = [16, 'crop_rainfed_tree']
esacci_to_glc2000_correspondence[20] = [16, 'crop_irrigated']
esacci_to_glc2000_correspondence[30] = [17, 'crop_natural_mosaic']
esacci_to_glc2000_correspondence[40] = [17, 'natural_crop_mosaic']
esacci_to_glc2000_correspondence[50] = [1, 'tree_broadleaved_evergreen']
esacci_to_glc2000_correspondence[60] = [2, 'tree_broadleaved_deciduous_closed_to_open_15']
esacci_to_glc2000_correspondence[61] = [2, 'tree_broadleaved_deciduous_closed_40']
esacci_to_glc2000_correspondence[62] = [5, 'tree_broadleaved_deciduous_open_15_40']
esacci_to_glc2000_correspondence[70] = [5, 'tree_needleleaved_deciduous_closed_to_open_15']
esacci_to_glc2000_correspondence[71] = [4, 'tree_needleleaved_evergreen_closed_to_open_15_extended']
esacci_to_glc2000_correspondence[72] = [4, 'tree_needleleaved_evergreen_open_15_40']
esacci_to_glc2000_correspondence[80] = [5, 'tree_needleleaved_deciduous_closed_to_open_15']
esacci_to_glc2000_correspondence[81] = [5, 'tree_needleleaved_deciduous_closed_40']
esacci_to_glc2000_correspondence[82] = [5, 'tree_needleleaved_deciduous_open_15_40']
esacci_to_glc2000_correspondence[90] = [6, 'tree_mixed_type']
esacci_to_glc2000_correspondence[100] = [9, 'mosaic_tree_and_shrub_50_herbaceous_cover_50']
esacci_to_glc2000_correspondence[110] = [9, 'mosaic_herbaceous_cover_50_tree_and_shrub_50']
esacci_to_glc2000_correspondence[120] = [12, 'shrubland']
esacci_to_glc2000_correspondence[121] = [11, 'evergreen_shrubland']
esacci_to_glc2000_correspondence[122] = [12, 'deciduous_shrubland']
esacci_to_glc2000_correspondence[130] = [13, 'grassland']
esacci_to_glc2000_correspondence[140] = [13, 'lichens_and_mosses']
esacci_to_glc2000_correspondence[150] = [13, 'sparse_vegetation_tree_shrub_herbaceous_cover_15']
esacci_to_glc2000_correspondence[151] = [14, 'sparse_tree_15']
esacci_to_glc2000_correspondence[152] = [14, 'sparse_shrub_15']
esacci_to_glc2000_correspondence[153] = [14, 'sparse_herbaceous_cover_15']
esacci_to_glc2000_correspondence[160] = [7, 'tree_cover_flooded_fresh_or_brakish_water']
esacci_to_glc2000_correspondence[170] = [8, 'tree_cover_flooded_saline_water']
esacci_to_glc2000_correspondence[180] = [15, 'shrub_or_herbaceous_cover_flooded_fresh_saline_brakish_water']
esacci_to_glc2000_correspondence[190] = [22, 'urban_areas']
esacci_to_glc2000_correspondence[200] = [19, 'bare_areas']
esacci_to_glc2000_correspondence[201] = [19, 'consolidated_bare_areas']
esacci_to_glc2000_correspondence[202] = [19, 'unconsolidated_bare_areas']
esacci_to_glc2000_correspondence[210] = [20, 'water_bodies']
esacci_to_glc2000_correspondence[220] = [21, 'permanent_snow_and_ice']


soilgrid_variable_names = [
    'ACDWRB',
    'AWCh1',
    'AWCh2',
    'AWCh3',
    'BDRICM',
    'BDRLOG',
    'BDTICM',
    'BLDFIE',
    'CECSOL',
    'CLYPPT',
    'CRFVOL',
    'HISTPR',
    'OCDENS',
    'OCSTHA',
    'ORCDRC',
    'PHIHOX',
    'PHIKCL',
    'SLGWRB',
    'SLTPPT',
    'SNDPPT',
    'TAXOUSDA',
    'TAXNWRB',
    'TEXMHT',
    'WWP',
]

soilgrid_variable_descriptions = OrderedDict()

soilgrid_variable_descriptions['ACDWRB'] = 'Grade of a sub-soil being acid e.g. having a pH < 5 and low BS:'
soilgrid_variable_descriptions['AWCh1'] = 'Available soil water capacity (volumetric fraction) with FC = pF 2.0: grade'
soilgrid_variable_descriptions['AWCh2'] = 'Available soil water capacity (volumetric fraction) with FC = pF 2.3: percentage'
soilgrid_variable_descriptions['AWCh3'] = 'Available soil water capacity (volumetric fraction) with FC = pF 2.5: percentage'
soilgrid_variable_descriptions['BDRICM'] = 'Depth to bedrock (R horizon) up to 200 cm: percentage'
soilgrid_variable_descriptions['BDRLOG'] = 'Probability of occurrence of R horizon: cm'
soilgrid_variable_descriptions['BDTICM'] = 'Absolute depth to bedrock: percentage'
soilgrid_variable_descriptions['BLDFIE'] = 'Bulk density (fine earth): cm'
soilgrid_variable_descriptions['CECSOL'] = 'Cation Exchange Capacity of soil: kg/m3'
soilgrid_variable_descriptions['CLYPPT'] = 'Weight percentage of the clay particles (<0.0002 mm): cmolc/kg'
soilgrid_variable_descriptions['CRFVOL'] = 'Volumetric percentage of coarse fragments (>2 mm): percentage'
soilgrid_variable_descriptions['HISTPR'] = 'Histosols probability cumulative: percentage'
soilgrid_variable_descriptions['OCDENS'] = 'Soil organic carbon density: percentage'
soilgrid_variable_descriptions['OCSTHA'] = 'Soil organic carbon stock: kg/m3'
soilgrid_variable_descriptions['ORCDRC'] = 'Soil organic carbon content: ton/ha'
soilgrid_variable_descriptions['PHIHOX'] = 'pH index measured in water solution: permille'
soilgrid_variable_descriptions['PHIKCL'] = 'pH index measured in KCl solution: pH'
soilgrid_variable_descriptions['SLGWRB'] = 'Sodic soil grade: pH'
soilgrid_variable_descriptions['SLTPPT'] = 'Weight percentage of the silt particles (0.0002–0.05 mm): grade'
soilgrid_variable_descriptions['SNDPPT'] = 'Weight percentage of the sand particles (0.05–2 mm): percentage'
soilgrid_variable_descriptions['TAXOUSDA'] = 'Keys to Soil Taxonomy suborders: percentage'
soilgrid_variable_descriptions['TAXNWRB'] = 'World Reference Base legend: -'
soilgrid_variable_descriptions['TEXMHT'] = 'Texture class (USDA system): -'
soilgrid_variable_descriptions['WWP'] = 'Available soil water capacity (volumetric fraction) until wilting point: -'



nlcd_colors = OrderedDict()
nlcd_colors[0] = [0,0,0]
nlcd_colors[1] = [0,249,0]
nlcd_colors[11] = [71,107,160]
nlcd_colors[12] = [209,221,249]
nlcd_colors[21] = [221,201,201]
nlcd_colors[22] = [216,147,130]
nlcd_colors[23] = [237,0,0]
nlcd_colors[24] = [170,0,0]
nlcd_colors[31] = [178,173,163]
nlcd_colors[32] = [249,249,249]
nlcd_colors[41] = [104,170,99]
nlcd_colors[42] = [28,99,48]
nlcd_colors[43] = [181,201,142]
nlcd_colors[51] = [165,140,48]
nlcd_colors[52] = [204,186,124]
nlcd_colors[71] = [226,226,193]
nlcd_colors[72] = [201,201,119]
nlcd_colors[73] = [153,193,71]
nlcd_colors[74] = [119,173,147]
nlcd_colors[81] = [219,216,61]
nlcd_colors[82] = [170,112,40]
nlcd_colors[90] = [186,216,234]
nlcd_colors[91] = [181,211,229]
nlcd_colors[92] = [181,211,229]
nlcd_colors[93] = [181,211,229]
nlcd_colors[94] = [181,211,229]
nlcd_colors[95] = [112,163,186]


nlcd_category_names = OrderedDict()
nlcd_category_names[0] = 'ndv'
nlcd_category_names[11] = 'Open Water'
nlcd_category_names[12] = 'Perennial Ice/Snow'
nlcd_category_names[21] = 'Developed, Open Space'
nlcd_category_names[22] = 'Developed, Low Intensity'
nlcd_category_names[23] = 'Developed, Medium Intensity'
nlcd_category_names[24] = 'Developed High Intensity'
nlcd_category_names[31] = 'Barren Land (Rock/Sand/Clay)'
nlcd_category_names[41] = 'Deciduous Forest'
nlcd_category_names[42] = 'Evergreen Forest'
nlcd_category_names[43] = 'Mixed Forest'
nlcd_category_names[51] = 'Dwarf Scrub'
nlcd_category_names[52] = 'Shrub/Scrub'
nlcd_category_names[71] = 'Grassland/Herbaceous'
nlcd_category_names[72] = 'Sedge/Herbaceous'
nlcd_category_names[73] = 'Lichens'
nlcd_category_names[74] = 'Moss'
nlcd_category_names[81] = 'Pasture/Hay'
nlcd_category_names[82] = 'Cultivated Crops'
nlcd_category_names[90] = 'Woody Wetlands'
nlcd_category_names[95] = 'Emergent Herbaceous Wetlands'

nlcd_category_descriptions = OrderedDict()
nlcd_category_descriptions[0] = 'ndv'
nlcd_category_descriptions[11] = 'areas of open water, generally with less than 25% cover of vegetation or soil.'
nlcd_category_descriptions[12] = 'areas characterized by a perennial cover of ice and/or snow, generally greater than 25% of total cover.'
nlcd_category_descriptions[21] = 'areas with a mixture of some constructed materials, but mostly vegetation in the form of lawn grasses. Impervious surfaces account for less than 20% of total cover. These areas most commonly include large-lot single-family housing units, parks, golf courses, and vegetation planted in developed settings for recreation, erosion control, or aesthetic purposes.'
nlcd_category_descriptions[22] = 'areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 20% to 49% percent of total cover. These areas most commonly include single-family housing units.'
nlcd_category_descriptions[23] = 'areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 50% to 79% of the total cover. These areas most commonly include single-family housing units.'
nlcd_category_descriptions[24] = 'highly developed areas where people reside or work in high numbers. Examples include apartment complexes, row houses and commercial/industrial. Impervious surfaces account for 80% to 100% of the total cover.'
nlcd_category_descriptions[31] = 'areas of bedrock, desert pavement, scarps, talus, slides, volcanic material, glacial debris, sand dunes, strip mines, gravel pits and other accumulations of earthen material. Generally, vegetation accounts for less than 15% of total cover.'
nlcd_category_descriptions[41] = 'areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species shed foliage simultaneously in response to seasonal change.'
nlcd_category_descriptions[42] = 'areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species maintain their leaves all year. Canopy is never without green foliage.'
nlcd_category_descriptions[43] = 'areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. Neither deciduous nor evergreen species are greater than 75% of total tree cover.'
nlcd_category_descriptions[51] = 'Alaska only areas dominated by shrubs less than 20 centimeters tall with shrub canopy typically greater than 20% of total vegetation. This type is often co-associated with grasses, sedges, herbs, and non-vascular vegetation.'
nlcd_category_descriptions[52] = 'areas dominated by shrubs; less than 5 meters tall with shrub canopy typically greater than 20% of total vegetation. This class includes true shrubs, young trees in an early successional stage or trees stunted from environmental conditions.'
nlcd_category_descriptions[71] = 'areas dominated by gramanoid or herbaceous vegetation, generally greater than 80% of total vegetation. These areas are not subject to intensive management such as tilling, but can be utilized for grazing.'
nlcd_category_descriptions[72] = 'Alaska only areas dominated by sedges and forbs, generally greater than 80% of total vegetation. This type can occur with significant other grasses or other grass like plants, and includes sedge tundra, and sedge tussock tundra.'
nlcd_category_descriptions[73] = 'Alaska only areas dominated by fruticose or foliose lichens generally greater than 80% of total vegetation.'
nlcd_category_descriptions[74] = 'Alaska only areas dominated by mosses, generally greater than 80% of total vegetation.'
nlcd_category_descriptions[81] = 'areas of grasses, legumes, or grass-legume mixtures planted for livestock grazing or the production of seed or hay crops, typically on a perennial cycle. Pasture/hay vegetation accounts for greater than 20% of total vegetation.'
nlcd_category_descriptions[82] = 'areas used for the production of annual crops, such as corn, soybeans, vegetables, tobacco, and cotton, and also perennial woody crops such as orchards and vineyards. Crop vegetation accounts for greater than 20% of total vegetation. This class also includes all land being actively tilled.'
nlcd_category_descriptions[90] = 'areas where forest or shrubland vegetation accounts for greater than 20% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.'
nlcd_category_descriptions[95] = 'Areas where perennial herbaceous vegetation accounts for greater than 80% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.'

e = 2.71828182845904523536028747135266249775724709369995
pi = 3.14159265358979323846264338327950288419716939937510

luh_data_dir = os.path.join(BASE_DATA_DIR, 'luh2', 'raw_data')
# Corresponds to a directory containing the latest LUH data download of states.nc and management.nc from maryland website
luh_scenario_names = [
    "RCP26_SSP1",
    "RCP34_SSP4",
    "RCP45_SSP2",
    "RCP60_SSP4",
    "RCP70_SSP3",
    "RCP85_SSP5",
    # "historical",
]

luh_scenario_states_paths = OrderedDict()
luh_scenario_states_paths['RCP26_SSP1'] = os.path.join(luh_data_dir, 'RCP26_SSP1', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-IMAGE-ssp126-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['RCP34_SSP4'] = os.path.join(luh_data_dir, 'RCP34_SSP4', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-GCAM-ssp434-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['RCP45_SSP2'] = os.path.join(luh_data_dir, 'RCP45_SSP2', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-MESSAGE-ssp245-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['RCP60_SSP4'] = os.path.join(luh_data_dir, 'RCP60_SSP4', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-GCAM-ssp460-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['RCP70_SSP3'] = os.path.join(luh_data_dir, 'RCP70_SSP3', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-AIM-ssp370-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['RCP85_SSP5'] = os.path.join(luh_data_dir, 'RCP85_SSP5', r"multiple-states_input4MIPs_landState_ScenarioMIP_UofMD-MAGPIE-ssp585-2-1-f_gn_2015-2100.nc")
luh_scenario_states_paths['historical'] = os.path.join(luh_data_dir, 'historical', r"states.nc")

luh_scenario_management_paths = OrderedDict()
luh_scenario_management_paths['RCP26_SSP1'] = os.path.join(luh_data_dir, 'RCP26_SSP1', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-IMAGE-ssp126-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['RCP34_SSP4'] = os.path.join(luh_data_dir, 'RCP34_SSP4', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-GCAM-ssp434-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['RCP45_SSP2'] = os.path.join(luh_data_dir, 'RCP45_SSP2', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-MESSAGE-ssp245-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['RCP60_SSP4'] = os.path.join(luh_data_dir, 'RCP60_SSP4', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-GCAM-ssp460-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['RCP70_SSP3'] = os.path.join(luh_data_dir, 'RCP70_SSP3', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-AIM-ssp370-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['RCP85_SSP5'] = os.path.join(luh_data_dir, 'RCP85_SSP5', r"multiple-management_input4MIPs_landState_ScenarioMIP_UofMD-MAGPIE-ssp585-2-1-f_gn_2015-2100.nc")
luh_scenario_management_paths['historical'] = os.path.join(luh_data_dir, 'historical', r"management.nc")

luh_state_names = [
    'primf',
    'primn',
    'secdf',
    'secdn',
    'urban',
    'c3ann',
    'c4ann',
    'c3per',
    'c4per',
    'c3nfx',
    'pastr',
    'range',
    'secmb',
    'secma',
]

luh_management_names = [
    'fertl_c3ann',
    'irrig_c3ann',
    'crpbf_c3ann',
    'fertl_c4ann',
    'irrig_c4ann',
    'crpbf_c4ann',
    'fertl_c3per',
    'irrig_c3per',
    'crpbf_c3per',
    'fertl_c4per',
    'irrig_c4per',
    'crpbf_c4per',
    'fertl_c3nfx',
    'irrig_c3nfx',
    'crpbf_c3nfx',
    'fharv_c3per',
    'fharv_c4per',
    'flood',
    'rndwd',
    'fulwd',
    'combf',
    'crpbf_total',
]



worldclim_bioclimatic_variable_names = OrderedDict()
worldclim_bioclimatic_variable_names[1] = 'Annual Mean Temperature'
worldclim_bioclimatic_variable_names[2] = 'Mean Diurnal Range (Mean of monthly (max temp - min temp))'
worldclim_bioclimatic_variable_names[3] = 'Isothermality (BIO2/BIO7) (* 100)'
worldclim_bioclimatic_variable_names[4] = 'Temperature Seasonality (standard deviation *100)'
worldclim_bioclimatic_variable_names[5] = 'Max Temperature of Warmest Month'
worldclim_bioclimatic_variable_names[6] = 'Min Temperature of Coldest Month'
worldclim_bioclimatic_variable_names[7] = 'Temperature Annual Range (BIO5-BIO6)'
worldclim_bioclimatic_variable_names[8] = 'Mean Temperature of Wettest Quarter'
worldclim_bioclimatic_variable_names[9] = 'Mean Temperature of Driest Quarter'
worldclim_bioclimatic_variable_names[10] = 'Mean Temperature of Warmest Quarter'
worldclim_bioclimatic_variable_names[11] = 'Mean Temperature of Coldest Quarter'
worldclim_bioclimatic_variable_names[12] = 'Annual Precipitation'
worldclim_bioclimatic_variable_names[13] = 'Precipitation of Wettest Month'
worldclim_bioclimatic_variable_names[14] = 'Precipitation of Driest Month'
worldclim_bioclimatic_variable_names[15] = 'Precipitation Seasonality (Coefficient of Variation)'
worldclim_bioclimatic_variable_names[16] = 'Precipitation of Wettest Quarter'
worldclim_bioclimatic_variable_names[17] = 'Precipitation of Driest Quarter'
worldclim_bioclimatic_variable_names[18] = 'Precipitation of Warmest Quarter'
worldclim_bioclimatic_variable_names[19] = 'Precipitation of Coldest Quarter'

countries_full_column_names = ['id', 'iso3', 'nev_name', 'fao_name', 'fao_id_c', 'gtap140', 'continent', 'region_un', 'region_wb', 'geom_index', 'abbrev', 'adm0_a3', 'adm0_a3_is', 'adm0_a3_un', 'adm0_a3_us', 'adm0_a3_wb', 'admin', 'brk_a3', 'brk_group', 'brk_name', 'country', 'disp_name', 'economy', 'fao_id', 'fao_reg', 'fips_10_', 'formal_en', 'formal_fr', 'gau', 'gdp_md_est', 'gdp_year', 'geounit', 'gu_a3', 'income_grp', 'iso', 'iso2_cull', 'iso3_cull', 'iso_3digit', 'iso_a2', 'iso_a3', 'iso_a3_eh', 'iso_n3', 'lastcensus', 'name', 'name_alt', 'name_ar', 'name_bn', 'name_cap', 'name_ciawf', 'name_de', 'name_el', 'name_en', 'name_es', 'name_fr', 'name_hi', 'name_hu', 'name_id', 'name_it', 'name_ja', 'name_ko', 'name_long', 'name_nl', 'name_pl', 'name_pt', 'name_ru', 'name_sort', 'name_sv', 'name_tr', 'name_vi', 'name_zh', 'ne_id', 'nev_lname', 'nev_sname', 'note_adm0', 'note_brk', 'official', 'olympic', 'pop_est', 'pop_rank', 'pop_year', 'postal', 'sov_a3', 'sovereignt', 'su_a3',
                               'subregion', 'subunit', 'type', 'un_a3', 'un_iso_n', 'un_vehicle', 'undp', 'uni', 'wb_a2', 'wb_a3', 'wiki1', 'wikidataid', 'wikipedia', 'woe_id', 'woe_id_eh', 'woe_note']

possible_shapefile_extensions = ['.shp', '.shx', '.dbf', '.prj', '.sbn', '.sbx', '.fbn', '.fbx', '.ain', '.aih', '.ixs', '.mxs', '.atx', '.shp.xml', '.cpg', '.qix']
common_gdal_readable_file_extensions = ['.tif', '.bil', '.adf', '.asc', '.hdf', '.nc',]
# gdal_readable_formats = ['AAIGrid', 'ACE2', 'ADRG', 'AIG', 'ARG', 'BLX', 'BAG', 'BMP', 'BSB', 'BT', 'CPG', 'CTG', 'DIMAP', 'DIPEx', 'DODS', 'DOQ1', 'DOQ2', 'DTED', 'E00GRID', 'ECRGTOC', 'ECW', 'EHdr', 'EIR', 'ELAS', 'ENVI', 'ERS', 'FAST', 'GPKG', 'GEORASTER', 'GRIB', 'GMT', 'GRASS', 'GRASSASCIIGrid', 'GSAG', 'GSBG', 'GS7BG', 'GTA', 'GTiff', 'GTX', 'GXF', 'HDF4', 'HDF5', 'HF2', 'HFA', 'IDA', 'ILWIS', 'INGR', 'IRIS', 'ISIS2', 'ISIS3', 'JDEM', 'JPEG', 'JPEG2000', 'JP2ECW', 'JP2KAK', 'JP2MrSID', 'JP2OpenJPEG', 'JPIPKAK', 'KEA', 'KMLSUPEROVERLAY', 'L1B', 'LAN', 'LCP', 'Leveller', 'LOSLAS', 'MBTiles', 'MAP', 'MEM', 'MFF', 'MFF2 (HKV)', 'MG4Lidar', 'MrSID', 'MSG', 'MSGN', 'NDF', 'NGSGEOID', 'NITF', 'netCDF', 'NTv2', 'NWT_GRC', 'NWT_GRD', 'OGDI', 'OZI', 'PCIDSK', 'PCRaster', 'PDF', 'PDS', 'PLMosaic', 'PostGISRaster', 'Rasterlite', 'RIK', 'RMF', 'ROI_PAC', 'RPFTOC', 'RS2', 'RST', 'SAGA', 'SAR_CEOS', 'SDE', 'SDTS', 'SGI', 'SNODAS', 'SRP', 'SRTMHGT', 'USGSDEM', 'VICAR', 'VRT', 'WCS', 'WMS', 'XYZ', 'ZMap',]