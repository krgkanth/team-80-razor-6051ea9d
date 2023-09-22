import logging

DEFAULT_X_COORDINATE : int = 4
DEFAULT_Y_COORDINATE : int = 4

class Position:
    x_coordinate : int = 0
    y_coordinate : int = 0

    def __init__(self, x_coordinate : int, y_coordinate : int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __getitem__(self, item):
        if item == 0:
            return self.x_coordinate
        elif item == 1:
            return self.y_coordinate
        else:
            raise Exception("Invalid tuple")

    def __eq__(self, other): 
        if not isinstance(other, Position):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate