from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError("Implement get_area function!")

class Width(ABC):
    @abstractmethod
    def set_width(self, width):
        raise NotImplementedError("Implement set_width function!")

class Height(ABC):
    @abstractmethod
    def set_height(self, height):
        raise NotImplementedError("Implement set_height function!")

class Circle(Shape, Width, Height):
    def __init__(self, radius):
        self.radius = radius

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

    def get_area(self):
        return math.pi * self.radius**2
    
class Square(Shape, Width, Height):
    def __init__(self, length):
        self.length = length

    def set_width(self, width):
        self.length = width
    
    def set_height(self, height):
        self.length = height

    def get_area(self):
        return self.length**2
    
class Rectangle(Shape, Width, Height):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.length * self.width
    
class Triangle(Shape, Height):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.length * self.width

# if all side of a shape and angles are the same, you can get the area with a formula to keep LSP compliant
class NewPolygon(Shape, Width):
    def __init__(self, n, width):
        self.n = n
        self.width = width

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return 0.25 * self.n * self.width**2 / math.tan(math.pi / self.n)
    
def main():
    circle = Circle(2)
    square = Square(2)
    rectangle = Rectangle(2, 4)
    # hexagon (6 sides) with a width of 1 unit for each side
    polygon = NewPolygon(6, 1)

    shapes = [circle, square, rectangle, polygon]

    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is: {shape.get_area()}")

if __name__ == "__main__":
    main()