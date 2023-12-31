"""Write a function which take a number as input to check if the given number is palindrome or
not and return back the result as bool."""


def reverse(n):
    rev_num = 0
    while n > 0:#101
        rev_num = rev_num * 10 + n % 10#1 #10 #101
        n = n // 10#10 #1

    return rev_num


def palindrome(n):
    rev_n = reverse(n)
    return rev_n == n


a = int(input("Enter Number :"))
print(f"{a} is Palindrome: {palindrome(a)}",)
