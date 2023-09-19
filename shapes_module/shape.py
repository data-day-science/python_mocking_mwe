from ._base import IShape

class Shape(IShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return "Shape at ({}, {})".format(self.x, self.y)