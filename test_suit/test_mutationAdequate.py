import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class MutationAdequateTest(unittest.TestCase):

    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type(2)
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(1, 0, 0)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(10, 11, 12)
        expected = Triangle.Type(1)
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(2, 2, 6)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type(2)
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(1, 1, 0)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(10, 11, 12)
        expected = Triangle.Type(1)
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(12, 13, 13)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(13, 12, 13)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

    def test13(self):
        actual = Triangle.classify(13, 13, 12)
        expected = Triangle.Type(3)
        self.assertEqual(actual, expected)

    def test14(self):
        actual = Triangle.classify(6, 3, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test15(self):
        actual = Triangle.classify(3, 6, 3)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

    def test16(self):
        actual = Triangle.classify(3, 3, 6)
        expected = Triangle.Type(0)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()