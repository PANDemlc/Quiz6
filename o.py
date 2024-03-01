from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length**2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
def main():
    circle = Circle(2)
    square = Square(2)
    rectangle = Rectangle(2, 4)

    shapes = [circle, square, rectangle]

    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is: {shape.get_area()}")

if __name__ == "__main__":
    main()