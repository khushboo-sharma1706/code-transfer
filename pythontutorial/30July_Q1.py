# class HelloWorld:
#     def __init__(self, name):
#         self.name = name
#
#     def print_name(self):
#         print(f"Hello World {self.name}!")
#
#     def print_double_name(self):
#         print(f"Hello World {self.name} {self.name}!")
#
#
# hello_world_k = HelloWorld("Khushboo")
# hello_world_k.print_name()
# hello_world_k.print_double_name()
#
# hello_world_g = HelloWorld("Gauri")
# hello_world_g.print_name()
#
#
# def print_name(name):
#     return f"Hello World {name}!"
#
#
# def print_double_name(name):
#     print(f"Hello World {name} {name}!")
#
#
# print(print_name("Khushboo"))
# print_double_name("Khushboo")


# Create a class for Animal (Type, Speed, Color), and a method to increase speed by 10 on call
# current speed of {type} is {speed}
class Animal:
    def __init__(self, type, speed, color):
        self.type = type
        self.speed = speed
        self.color = color

    def speed_1(self):
        self.speed += 10

    def current_speed(self):
        print(f"Current speed of {self.type} is {self.speed}")


dog = Animal("dog", 50, "Black")
dog.current_speed()
dog.speed_1()
dog.current_speed()
print(dog.speed)
