import unittest
from points_rules import (
    points_for_alphanumeric,
    points_if_whole_number,
    points_if_multiple_of_pointtwofive,
    points_for_every_two_items,
    points_based_on_name_of_items,
    points_based_on_date,
    points_based_on_time,
)

class TestPointsRules(unittest.TestCase):

    def test_points_for_alphanumeric(self):
        self.assertEqual(points_for_alphanumeric("abc123"), 6)
        self.assertEqual(points_for_alphanumeric("abc"), 3)
        self.assertEqual(points_for_alphanumeric("123"), 3)
        self.assertEqual(points_for_alphanumeric(""), 0)

    def test_points_if_whole_number(self):
        
        self.assertEqual(points_if_whole_number(10.0), 50)
        self.assertEqual(points_if_whole_number(10.5), 0)
        self.assertEqual(points_if_whole_number(0.0), 50)
        self.assertEqual(points_if_whole_number(-10.0), 50)

    def test_points_if_multiple_of_pointtwofive(self):
        self.assertEqual(points_if_multiple_of_pointtwofive(0.25), 25)
        self.assertEqual(points_if_multiple_of_pointtwofive(0.5), 25)
        self.assertEqual(points_if_multiple_of_pointtwofive(0.75), 25)
        self.assertEqual(points_if_multiple_of_pointtwofive(1.0), 25)
        self.assertEqual(points_if_multiple_of_pointtwofive(1.25), 25)
        self.assertEqual(points_if_multiple_of_pointtwofive(1.4), 0)

    def test_points_for_every_two_items(self):
        self.assertEqual(points_for_every_two_items([]), 0)
        self.assertEqual(points_for_every_two_items([1]), 0)
        self.assertEqual(points_for_every_two_items([1, 2]), 5)
        self.assertEqual(points_for_every_two_items([1, 2, 3, 4]), 10)

    def test_points_based_on_name_of_items(self):
        self.assertEqual(points_based_on_name_of_items("abc", 10.0), 2)
        self.assertEqual(points_based_on_name_of_items("abcdef", 10.0), 2)
        self.assertEqual(points_based_on_name_of_items("abc", 5.0), 1)

    def test_points_based_on_date(self):
        self.assertEqual(points_based_on_date("2022-01-01"), 6)
        self.assertEqual(points_based_on_date("2022-01-02"), 0)
        self.assertEqual(points_based_on_date("2022-01-03"), 6)
        self.assertEqual(points_based_on_date("2022-01-04"), 0)

    def test_points_based_on_time(self):
        self.assertEqual(points_based_on_time("13:00"), 0)
        self.assertEqual(points_based_on_time("14:00"), 10)
        self.assertEqual(points_based_on_time("15:00"), 10)
        self.assertEqual(points_based_on_time("16:00"), 10)
        self.assertEqual(points_based_on_time("17:00"), 0)

if __name__ == "__main__":
    unittest.main()