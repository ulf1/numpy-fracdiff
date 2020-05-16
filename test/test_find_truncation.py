from numpy_fracdiff.find_truncation import find_truncation
import numpy.testing as npt


def test0():
    m, w = find_truncation(0)
    npt.assert_allclose(m, 0)
    npt.assert_allclose(w, [1.0])


def test1():
    m, w = find_truncation(1)
    npt.assert_allclose(m, 1)
    npt.assert_allclose(w, [1.0, -1.0])


def test2():
    m, w = find_truncation(2)
    npt.assert_allclose(m, 2)
    npt.assert_allclose(w, [1.0, -2.0, 1.0])


def test3():
    m, w = find_truncation(3)
    npt.assert_allclose(m, 3)
    npt.assert_allclose(w, [1.0, -3.0, 3.0, -1.0])


def test4():
    m, w = find_truncation(4)
    npt.assert_allclose(m, 4)
    npt.assert_allclose(w, [1.0, -4.0, 6.0, -4.0, 1.0])
