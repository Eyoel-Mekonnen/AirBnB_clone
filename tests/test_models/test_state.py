#!/usr/bin/python3
"""Unittest for the class state"""


class test_state(unittest.TestCase):
    """unittest for test class begins here"""
    
    def test_state_creation(self):
        """tests if state instance is created"""
        state = State()
        name = "Alabama"
        state.name = name
        self.asserEqual(state.name, name)
