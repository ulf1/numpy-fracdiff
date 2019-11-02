import unittest
from fracdiff.fracdiff_fn import fracdiff
import numpy as np
import numpy.testing as npt


class Test_fracdiff_fn(unittest.TestCase):

    def test1(self):
        x = np.array([10, 11, 9])
        w = [1.0, -1.0]
        z = fracdiff(x, weights=w)
        target = np.array([np.nan, 1.0, -2.0])
        npt.assert_allclose(z, target)

    def test2(self):
        x = np.array([10, 11, 9])
        w = [1.0, -2.0, 1.0]
        z = fracdiff(x, weights=w)
        target = np.array([np.nan, np.nan, -3.0])
        npt.assert_allclose(z, target)

    def test3(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=1, truncation='find')
        target = np.array([np.nan, 1.0, -2.0])
        npt.assert_allclose(z, target)

    def test4(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=2, truncation='find')
        target = np.array([np.nan, np.nan, -3.0])
        npt.assert_allclose(z, target)

    def test5(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=1, truncation=1)
        target = np.array([np.nan, 1.0, -2.0])
        npt.assert_allclose(z, target)

    def test6(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=2, truncation=2)
        target = np.array([np.nan, np.nan, -3.0])
        npt.assert_allclose(z, target)

    def test7(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=1)
        target = np.array([np.nan, 1.0, -2.0])
        npt.assert_allclose(z, target)

    def test8(self):
        x = np.array([10, 11, 9])
        z = fracdiff(x, order=2)
        target = np.array([np.nan, np.nan, -3.0])
        npt.assert_allclose(z, target)

    def test11(self):
        X = np.array([[10, 11, 9], [4, 6, 9]]).T
        Z = fracdiff(X, order=1)
        target = np.array([[np.nan, 1.0, -2.0], [np.nan, 2.0, 3.0]]).T
        npt.assert_allclose(Z, target)


# run
if __name__ == '__main__':
    unittest.main()
