# Write a class with three numbers as member of that (a, b, c) and two methods (min and max),
# both of them supposed to return the min and max of all three numbers respectively.

class MyClass:

    def max(a, b, c):
        if (a >= b) and (a >= c):
            maximum = a
        elif (b >= a) and (b >= c):
            maximum = b
        else:
            maximum = c
        return maximum

    def min(a, b, c):
        if (a <= b) and (a <= c):
            minimum = a

        elif (b <= a) and (b <= c):
            minimum = b
        else:
            minimum = c
        return minimum


a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))

print(max(a, b, c))
print(min(a, b, c))
