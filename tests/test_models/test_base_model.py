#!/usr/bin/python3
"""Unittesting for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test case for base model will be conducted"""

    def test_creation_of_instance(self):
        """checking instance"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
    
    def test_the_str_method(self):
        """Tests the str method in BaseModel"""
        base = BaseModel()
        base.id = "101112"
        string_iso = datetime(2024, 3, 5, 17, 10, 9, 619532).isoformat()
        base.created_at = string_iso
        base.updated_at = string_iso
        dict_ = base.__str__()
        self.assertEqual("[BaseModel] (101112) {'id': '101112', 'created_at': '2024-03-05T17:10:09.619532', 'updated_at': '2024-03-05T17:10:09.619532'}", dict_)
    
    def test_save_method(self):
        """tests the save method of BaseModel"""
        base = BaseModel()
        original_time =base.updated_at
        base.save()
        time.sleep(1)
        self.assertTrue(original_time < base.updated_at)

    def test_to_dict(self):
        """Tests the converstion of an object to dictionary representation"""
        time_stamp = datetime.today()
        base = BaseModel()
        base.id = "101112"
        base.created_at = time_stamp
        base.updated_at = time_stamp
        self.assertEqual({'id': '101112', '__class__': 'BaseModel', 'created_at': time_stamp.isoformat(), 'updated_at': time_stamp.isoformat()}, base.to_dict())



