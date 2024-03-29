#!/usr/bin/python3
"""Test case using Unittest for user"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class Test_User_class_creation(unittest.TestCase):
    """checking using unittest the instance creation"""

    def test_user_email(self):
        user = User()
        test_email = 'ey@gmail.com'
        user.email = test_email
        password = '123'
        user.password = '123'
        first_name = 'john'
        user.first_name = first_name
        last_name = 'Doe'
        user.last_name = last_name
        self.assertEqual(user.email, test_email)
        self.assertEqual(user.password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
