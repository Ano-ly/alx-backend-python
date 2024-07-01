#!/usr/bin/env python3
"""Test method for access_nested_map"""
import unittest
from parameterized import parameterized
a_n_m = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, the_map, path, expected):
        """Test access_nested map function"""
        self.assertEqual(a_n_m(the_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, the_map, path, message):
        """Test that KeyError is raised with the above inputs"""
        a_n_m(the_map, path)
        self.assertRaises(KeyError, message)


if __name__ == "__main__":
    unittest.main()
