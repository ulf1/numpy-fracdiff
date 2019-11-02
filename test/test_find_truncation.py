import unittest
from fracdiff.find_truncation import find_truncation


class Test_find_truncation(unittest.TestCase):

    def test0(self):
        m, w = find_truncation(0)
        self.assertEquals(m, 0)
        self.assertEquals(w, [1.0])

    def test1(self):
        m, w = find_truncation(1)
        self.assertEquals(m, 1)
        self.assertEquals(w, [1.0, -1.0])

    def test2(self):
        m, w = find_truncation(2)
        self.assertEquals(m, 2)
        self.assertEquals(w, [1.0, -2.0, 1.0])

    def test3(self):
        m, w = find_truncation(3)
        self.assertEquals(m, 3)
        self.assertEquals(w, [1.0, -3.0, 3.0, -1.0])

    def test4(self):
        m, w = find_truncation(4)
        self.assertEquals(m, 4)
        self.assertEquals(w, [1.0, -4.0, 6.0, -4.0, 1.0])


# run
if __name__ == '__main__':
    unittest.main()
