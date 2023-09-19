from abc import ABCMeta, abstractmethod

class IShape(metaclass=ABCMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass