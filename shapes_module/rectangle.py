from .shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return "Rectangle at ({}, {}) with width {} and height {}".format(self.x, self.y, self.width, self.height)