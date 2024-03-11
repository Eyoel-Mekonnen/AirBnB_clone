#!/usr/bin/python3
"""Unittest for amenity is being created"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class Test_case_Amenity_class(unittest.TestCase):
    """class for amenity class checking is defined"""

    def test_amenity_instance_creation(self):
        """method to determine if amenity is created"""
        amenity = Amenity()
        name = "cassanova"
        amenity.name = name
        self.assertEqual(amenity.name, name)
