from .shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return "Circle at ({}, {}) with radius {}".format(self.x, self.y, self.radius)
    
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Circle) and self.x == __value.x and self.y == __value.y and self.radius == __value.radius