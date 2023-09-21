from unittest import TestCase
from levelup.position import Position

class TestPositionDefaultCoordinates(TestCase):


    def test_specific(self):
        specific_x_coordinate = 8
        specific_y_coordinate = 9
        testobj = Position(specific_x_coordinate, specific_y_coordinate)
        self.assertEqual(specific_x_coordinate, testobj.x_coordinate)
        self.assertEqual(specific_y_coordinate, testobj.y_coordinate)

    def test_equality(self):
        position_a = Position(1,1)
        position_b = Position(1,1)

        self.assertEqual(position_a, position_b)
