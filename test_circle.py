"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class TestCircle(unittest.TestCase):
    def test_add_area(self):
        val1 = Circle(3)
        val2 = Circle(4)
        val3 = val1.add_area(val2)
        self.assertEqual(val3.get_radius(), 5)

    def test_area_edge_case(self):
        val1 = Circle(3)
        val2 = Circle(0)
        val3 = val1.add_area(val2)
        self.assertTrue(val3.get_radius(), 3)

    def test_negative(self):
        with self.assertRaises(ValueError):
            Circle(-1)


if __name__ == '__main__':
    unittest.main()
