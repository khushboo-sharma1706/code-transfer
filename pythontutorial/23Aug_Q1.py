"""1. Write a program to create a class called Shape with methods called getPerimeter()
and getArea(). Create a subclass called Circle that overrides the getPerimeter()
and getArea() methods to calculate the area and perimeter of a circle."""
import math


class Shape:
    def __init__(self):
        pass

    def getPerimeter(self):
        pass

    def getArea(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        super().__init__()

    def getArea(self):
        return math.pi * self.r ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.r


circle = Circle(3)
print(f"Area of Circle: {circle.getArea()}")
print(f"Perimeter of Circle: {circle.getPerimeter()}")
