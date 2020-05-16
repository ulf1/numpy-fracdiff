from numpy_fracdiff.frac_weights import frac_weights
import numpy.testing as npt


def test0():
    w = frac_weights(0, m=1)
    npt.assert_allclose(w, [1.0, 0.0])


def test1():
    w = frac_weights(1, m=2)
    npt.assert_allclose(w, [1.0, -1.0, 0.0])


def test2():
    w = frac_weights(2, m=3)
    npt.assert_allclose(w, [1.0, -2.0, 1.0, 0.0])


def test3():
    w = frac_weights(3, m=4)
    npt.assert_allclose(w, [1.0, -3.0, 3.0, -1.0, 0.0])


def test4():
    w = frac_weights(4, m=5)
    npt.assert_allclose(w, [1.0, -4.0, 6.0, -4.0, 1.0, 0.0])


def test5():
    w = frac_weights(0.5, m=3)
    npt.assert_allclose(w, [1.0, -0.5, -0.125, -0.0625])


def test6():
    w = frac_weights(1.5, m=3)
    npt.assert_allclose(w, [1.0, -1.5, 0.375, 0.0625])
