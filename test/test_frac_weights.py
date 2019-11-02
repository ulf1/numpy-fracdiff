import unittest
from fracdiff.frac_weights import frac_weights


class Test_find_truncation(unittest.TestCase):

    def test0(self):
        w = frac_weights(0, m=1)
        self.assertEquals(w, [1.0, 0.0])

    def test1(self):
        w = frac_weights(1, m=2)
        self.assertEquals(w, [1.0, -1.0, 0.0])

    def test2(self):
        w = frac_weights(2, m=3)
        self.assertEquals(w, [1.0, -2.0, 1.0, 0.0])

    def test3(self):
        w = frac_weights(3, m=4)
        self.assertEquals(w, [1.0, -3.0, 3.0, -1.0, 0.0])

    def test4(self):
        w = frac_weights(4, m=5)
        self.assertEquals(w, [1.0, -4.0, 6.0, -4.0, 1.0, 0.0])

    def test5(self):
        w = frac_weights(0.5, m=3)
        self.assertEquals(w, [1.0, -0.5, -0.125, -0.0625])

    def test6(self):
        w = frac_weights(1.5, m=3)
        self.assertEquals(w, [1.0, -1.5, 0.375, 0.0625])


# run
if __name__ == '__main__':
    unittest.main()
