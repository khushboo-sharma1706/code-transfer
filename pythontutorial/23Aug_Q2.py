"""2. Create a class named 'Shape' with a method to print "This is This is shape".
    Then create two other classes named 'Rectangle', 'Circle' inheriting the Shape class,
    both having a method to print "This is rectangular shape" and "This is circular shape"
    respectively. Create a subclass 'Square' of 'Rectangle' having a method to print
    "Square is a rectangle". Now call the method of 'Shape' and 'Rectangle' class by the object
    of 'Square' class."""


class Shape:
    def __init__(self):
        pass

    def print_ss(self):
        print("This is This is shape")


class Rectangle(Shape):
    def __init__(self):
        pass

    def print_r(self):
        print("This is rectangular shape")


class Circle(Shape):
    def __init__(self):
        pass

    def print_c(self):
        print("This is circular shape")


class Square(Rectangle):
    def __init__(self):
        pass

    def print_s(self):
        print("Square is a rectangle")

square = Square()
square.print_s()
square.print_r()
square.print_ss()
