#!/usr/bin/python3
"""unittest case for city class"""


class Test_case_City(unittest.TestCase):
    """Class for the unit test of class is created"""
    
    def test_city_instance_creation(self):
        """method of checking instance creation"""
        city = City()
        st_id = '123'
        city.state_id = st_id
        name = "JohnDoe"
        city.name = name
        self.assertEqual(city.state_id, st_id)
        self.assertEqual(city.name, name)
