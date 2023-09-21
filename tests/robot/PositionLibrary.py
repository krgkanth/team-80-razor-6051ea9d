from levelup.position import Position
from robot.libraries.BuiltIn import BuiltIn

class PositionLibrary:
    ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

    def initialize_position(self, x_coordinate, y_coordinate):
        self.position = Position(x_coordinate, y_coordinate)

    def starting_X_coordinate_should_be(self, expected):
        actual = self.position.x_coordinate
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def starting_Y_coordinate_should_be(self, expected):
        actual = self.position.y_coordinate
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"
