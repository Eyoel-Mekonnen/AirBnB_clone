#!/usr/bin/python3
"""Unittest for amenity is being created"""


class Test_case_Amenity_class(unittest.TestCase):
    """class for amenity class checking is defined"""

    def test_amenity_instance_creation(self):
        """method to determine if amenity is created"""
        amenity = Amenity()
        name = "cassanova"
        amenity.name = name
        self.assertEqual(amenity.name, name)
