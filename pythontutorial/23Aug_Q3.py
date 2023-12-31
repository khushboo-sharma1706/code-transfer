class Demo:
    def __init__(self):
        print("Demo's __init__() invoked")
class Derived_Demo(Demo):
    def __init__(self):
        super().__init__()
        print("Derived_Demo's __init__() invoked")

obj1 = Derived_Demo()
obj2 = Demo()
