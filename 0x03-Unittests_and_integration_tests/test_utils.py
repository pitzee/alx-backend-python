#!/usr/bin/env python3
""" Test for access_nested_map function  """
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


Class TestAccessNestedMap(unittest.TestCase):
    """ Tests the access_nested_map function """

    def TestAccessNestedMap.test_access_nested_map(self, nested_map: Mapping,path: Sequence, 
                                                        expected: int) -> None:
        """ Test the access_nested_map method. """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

        @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

