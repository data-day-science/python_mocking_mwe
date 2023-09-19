from .shape import Shape
from .circle import Circle
from .rectangle import Rectangle

class BagOfShapes:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        self.shapes.append(shape)
    
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total
    
    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total += shape.perimeter()
        return total
    
    def add_circle(self, x, y, radius):
        self.shapes.append(Circle(x, y, radius))

    def add_rectangle(self, x, y, width, height):
        self.shapes.append(Rectangle(x, y, width, height))

    def __str__(self):
        return "Bag of shapes with {} shapes".format(len(self.shapes))
    
    