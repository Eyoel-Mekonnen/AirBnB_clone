#!/usr/bin/python3
"""Unittesting for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import os
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test case for base model will be conducted"""

    def test_creation_of_instance(self):
        """checking instance"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_str_representation(self):
        """Checking the string representation of str"""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_save_method(self):
        """tests the save method of BaseModel"""
        base = BaseModel()
        original_time = base.updated_at
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
        self.assertEqual({'id': '101112', '__class__': 'BaseModel',
                         'created_at':
                          time_stamp.isoformat(), 'updated_at':
                          time_stamp.isoformat()}, base.to_dict())


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())
