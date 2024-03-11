#!/usr/bin/python3
"""unittest for class Review"""


class Test_case_Review_class(unittest.TestCase):
    """Test cases for review class"""

    def test_instance_creation_review(self):
        """checks the instance creation of review"""
        review = Review()
        place_id = "Va1002"
        review.place_id = place_id
        self.assertEqual(review.place_id, place_id)
        user_id = "123"
        review.user_id = user_id
        self.assertEqual(review.user_id, user_id)
        text = "Welcome"
        review.text = text
        self.assertEqual(review.text, text)
