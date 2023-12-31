class Animal:
    def __init__(self, speed):
        self.starting_point = 0
        self.speed = speed

    def sound(self):
        print("No Sound")

    def walk(self, time, rest_time=0):
        self.starting_point += self.speed * (time - rest_time)


class Dog(Animal):
    def __init__(self):
        super().__init__(4)

    def sound(self):
        print("Bhow Bhow!!")
        super().sound()

    def walk(self, time, rest_time=0):
        super().walk(time, rest_time)
        self.starting_point += 5


class Cat(Animal):
    def __init__(self):
        super().__init__(2)

    def sound(self):
        print("Meow Meow!!")


dog = Dog()
dog.walk(5)
print(dog.starting_point)
dog.walk(5, 4)
print(dog.starting_point)
dog.sound()

cat = Cat()
cat.walk(5)
print(cat.starting_point)
cat.sound()
