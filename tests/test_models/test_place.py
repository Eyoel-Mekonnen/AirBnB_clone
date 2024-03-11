#!/usr/bin/python3
"""Unittest case for the class Place"""


class Test_Place(unittest.TestCase):
    """unittest for the class begins here"""

    def test_instance_creation(self):
        """determines whether or not instance is created"""
        place = Place()
        city_id = "Va22003"
        place.city_id = city_id
        self.assertEqual(place.city_id, city_id)
        user_id = '123'
        place.user_id = user_id
        self.assertEqual(place.user_id, user_id)
        name = "Alexander"
        place.name = name
        self.assertEqual(place.name, name)
        description = "Apartement"
        place.description = description
        self.assertEqual(place.description, description)
        number_rooms = 5
        place.number_rooms = number_rooms
        self.assertEqual(place.number_rooms, number_rooms)
        number_bathrooms = 3
        place.number_bathrooms = number_bathrooms
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        max_guest = 5
        place.max_guest = max_guest
        self.assertEqual(place.max_guest, max_guest)
        price_by_night = 100
        place.price_by_night = price_by_night
        self.assertEqual(place.price_by_night, price_by_night)
        latitude = 37.23
        place.latitude = latitude
        self.assertEqual(place.latitude, latitude)
        longitude = 47.23
        self.assertEqual(place.longitude, longitude)
        amenity_ids = "123"
        place.amenity_ids = amenity_ids
        self.assertEqual(place.amenity_ids, amenity_ids)
