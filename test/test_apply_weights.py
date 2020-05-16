from numpy_fracdiff.apply_weights import apply_weights
import numpy as np
import numpy.testing as npt


def test1():
    x = np.array([10, 11, 9])
    w = np.array([1.0, -1.0])
    z = apply_weights(x, w)
    target = np.array([np.nan, 1.0, -2.0])
    npt.assert_allclose(z, target)


def test2():
    x = np.array([10, 11, 9])
    w = np.array([1.0, -2.0, 1.0])
    z = apply_weights(x, w)
    target = np.array([np.nan, np.nan, -3.0])
    npt.assert_allclose(z, target)
