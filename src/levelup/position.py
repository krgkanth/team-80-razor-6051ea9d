import logging

DEFAULT_X_COORDINATE : int = 4
DEFAULT_Y_COORDINATE : int = 4

class Position:
    x_coordinate : int = 0
    y_coordinate : int = 0

    def __init__(self, x_coordinate : int, y_coordinate : int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate