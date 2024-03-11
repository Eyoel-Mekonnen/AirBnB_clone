#!/usr/bin/python3
"""Unittest for the class state"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class test_state(unittest.TestCase):
    """unittest for test class begins here"""

    def test_state_creation(self):
        """tests if state instance is created"""
        state = State()
        name = "Alabama"
        state.name = name
        self.assertEqual(state.name, name)
