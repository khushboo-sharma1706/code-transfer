"""Write a function to accept a string and return a string made of the first 2 and last
2 characters of a given string. If the string length is less than 2, return the empty string."""


def string(n):
    if len(n) < 2:
        return ""
    else:
        return f"{n[:2]}{n[-2:]}"


print(string("Manthan"))
print(string("Khushboo"))
print(string("ManKhush"))