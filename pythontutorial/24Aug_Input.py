# print("Your Name: ", end="")
# a = input()
# a = input("Your Name: ")
# print(a)

def take_input(count):
    while True:
        try:
            val = int(input(f"Number {count}: "))
        except ValueError:
            print("Invalid Input! Retry")
        else:
            print("Right Input! Good Job")
            return val
        finally:
            print("Finally")


a = take_input(1)
b = take_input(2)
print(a + b)
