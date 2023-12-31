"""Q1: Write a program to print the area of a rectangle by creating a class named 'Area'
having two functions. First function named as 'setDim' takes the length and breadth of
the rectangle as parameters and the second function named as 'getArea' returns the area
of the rectangle."""


class Area:
    def __init__(self): #if __init__ kuch input ni leta to likhna jruri ni hota other we can pass if there is no body in init
        pass

    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        area = self.length * self.breadth
        return area

Area1 = Area()

Area1.setDim(4,5)
result = Area1.getArea()
print(result)

