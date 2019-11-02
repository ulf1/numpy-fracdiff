import unittest
from fracdiff.apply_weights import apply_weights
import numpy as np
import numpy.testing as npt


class Test_apply_weights(unittest.TestCase):

    def test1(self):
        x = np.array([10, 11, 9])
        w = [1.0, -1.0]
        z = apply_weights(x, w)
        target = np.array([np.nan, 1.0, -2.0])
        npt.assert_allclose(z, target)

    def test2(self):
        x = np.array([10, 11, 9])
        w = [1.0, -2.0, 1.0]
        z = apply_weights(x, w)
        target = np.array([np.nan, np.nan, -3.0])
        npt.assert_allclose(z, target)


# run
if __name__ == '__main__':
    unittest.main()
