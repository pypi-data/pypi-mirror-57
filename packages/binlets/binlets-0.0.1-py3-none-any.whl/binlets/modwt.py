from functools import reduce
from itertools import product

import numpy as np


def modwt_level(data, level, axis=-1, approx_only=False):
    """1D Haar MODWT transform.

    Parameters
    ----------
    data : numpy.array
        Input signal.
    level : int
    axis : int or tuple of ints
        Axis or axes along which elements are shifted.
        By default, last dimension.
    approx_only : bool
        Set to True to only calculate approximation coefficients.

    Returns
    -------
    numpy.array or tuple of numpy.array
        Aproximantion coefficients or
        tuple of approximation and defailt coefficients.
    """
    shifted = np.roll(data, -2 ** level, axis=axis)
    approx = (shifted + data)
    if approx_only:
        return approx
    else:
        detail = (shifted - data)
        return approx, detail


def imodwt_level(approx, detail, level, axis=-1):
    """Inverse 1D Haar MODWT transform.

    Parameters
    ----------
    approx, detail : numpy.array
        Approximation and detail coefficients.
    level : int
    axis : int or tuple of ints
        Axis or axes along which elements are shifted.
        By default, last dimension.

    Returns
    -------
    numpy.array
        Reconstructed signal.
    """
    data = (approx - detail) / 2
    shifted = np.roll((approx + detail) / 2, 2 ** level, axis=axis)
    return (data + shifted) / 2


def modwt_level_mask(mask, level, axis=-1):
    
    mask &= np.roll(mask, -2 ** level, axis=axis)
    return mask


def modwt_level_nd(data, level, axes, approx_only=False):
    """nD Haar MODWT transform.

    Parameters
    ----------
    axes : tuple
        Axes to apply the transform.
    approx_only : bool
        If True, returns only approximation coefficients.
    """
    if approx_only:
        return reduce(lambda approx, axis: modwt_level(approx, level, axis, approx_only=True), axes, data)

    coeffs = [('', data)]
    for axis in axes:
        new_coeffs = []
        for subband, x in coeffs:
            A, D = modwt_level(x, level, axis)
            new_coeffs.extend([(subband + 'a', A), (subband + 'd', D)])
        coeffs = new_coeffs
    return dict(coeffs)


def modwt_level_mask_nd(mask, level, axes):
    for axis in axes:
        mask = modwt_level_mask(mask, level, axis)
    return mask


def imodwt_level_nd(coeffs, level, axes):
    """nD Haar MODWT transform."""
    for key_length, axis in reversed(list(enumerate(axes))):
        new_coeffs = {}
        new_keys = [''.join(coef) for coef in product('ad', repeat=key_length)]
        for key in new_keys:
            A = coeffs.get(key + 'a')
            D = coeffs.get(key + 'd')
            new_coeffs[key] = imodwt_level(A, D, level, axis)
        coeffs = new_coeffs
    return coeffs['']
