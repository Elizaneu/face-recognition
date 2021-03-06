# Parameters
from src.classification.features import dct, dft, gradient, histogram, scale, show_dct, show_dft


P_HISTOGRAM = 'P_HISTOGRAM'
P_DFT = 'P_DFT'
P_DCT = 'P_DCT'
P_GRADIENT = 'P_GRADIENT'
P_SCALE = 'P_SCALE'
P_IMAGES_PER_PERSON = 'P_IMAGES_PER_PERSON'

R_METHOD_HISTOGRAM = "R_METHOD_HISTOGRAM"
R_METHOD_DCT = "R_METHOD_DCT"
R_METHOD_DFT = "R_METHOD_DFT"
R_METHOD_GRADIENT = "R_METHOD_GRADIENT"
R_METHOD_SCALE = "R_METHOD_SCALE"

ALL_METHODS = (R_METHOD_HISTOGRAM, R_METHOD_DCT,
               R_METHOD_DFT, R_METHOD_GRADIENT, R_METHOD_SCALE)

# Default parameters
PARAMS_DEFAULTS = {
    f"{P_HISTOGRAM}": 19,
    f"{P_DFT}": 20,
    f"{P_DCT}": 16,
    f"{P_GRADIENT}": 2,
    f"{P_SCALE}": 0.12,
    f"{P_IMAGES_PER_PERSON}": 5,
}

# Global application settings
PARAMS = {
    f"{P_HISTOGRAM}": PARAMS_DEFAULTS[f"{P_HISTOGRAM}"],
    f"{P_DFT}": PARAMS_DEFAULTS[f"{P_DFT}"],
    f"{P_DCT}": PARAMS_DEFAULTS[f"{P_DCT}"],
    f"{P_GRADIENT}": PARAMS_DEFAULTS[f"{P_GRADIENT}"],
    f"{P_SCALE}": PARAMS_DEFAULTS[f"{P_SCALE}"],
    f"{P_IMAGES_PER_PERSON}": PARAMS_DEFAULTS[f"{P_IMAGES_PER_PERSON}"],
}

METHOD_TO_FUNCTION_MAP = {
    R_METHOD_HISTOGRAM: histogram,
    R_METHOD_DCT: dct,
    R_METHOD_DFT: dft,
    R_METHOD_GRADIENT: gradient,
    R_METHOD_SCALE: scale,
}

METHOD_TO_PARAM_MAP = {
    R_METHOD_HISTOGRAM: P_HISTOGRAM,
    R_METHOD_DCT: P_DCT,
    R_METHOD_DFT: P_DFT,
    R_METHOD_GRADIENT: P_GRADIENT,
    R_METHOD_SCALE: P_SCALE,
}

SHOW_METHOD_TO_PARAM_MAP = {
    R_METHOD_HISTOGRAM: histogram,
    R_METHOD_DCT: show_dct,
    R_METHOD_DFT: show_dft,
    R_METHOD_GRADIENT: gradient,
    R_METHOD_SCALE: scale,
}
