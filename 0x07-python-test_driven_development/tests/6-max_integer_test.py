#!/usr/bin/python3
"""
Unittest for function max_integer
gets the maximum integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unittest for the function max_integer
    """
    def test_normal(self):
        """Normal case test"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_no_params(self):
        """Test with no Parameters"""
        self.assertEqual(max_integer(), None)

    def test_one_value(self):
        """Test with only one value"""
        self.assertEqual(max_integer([3]), 3)

    def test_neg_values(self):
        """Test with negative values"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_types(self):
        """Test with different data types"""
        with self.assertRaises(TypeError):
            max_integer([2, '7', 4])
        with self.assertRaises(TypeError):
            max_integer([1, [4, 7], 5])

    def test_with_float(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1, 2.8, 3, 4.7]), 4.7)

    def test_neg_pos(self):
        """Test with both negative and positive numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_not_list(self):
        """test with types which are not lists"""
        with self.assertRaises(TypeError):
            max_integer(9)

    def test_string(self):
        """Test with strings"""
        self.assertEqual(max_integer("String"), 't')

    def test_list_string(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["one", "two", "three", "four"]), "two")

    def test_None(self):
        """Test with None value"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    """if module is run as the main file"""
    unittest.main()
