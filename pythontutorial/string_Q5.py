# Write a function to check whether a string contains all letters of the alphabet.

def alp(s):
    for i in range(65, 91):
        if chr(i) not in s and chr(i + 32) not in s:
            print(i)
            return False
    return True


print(alp("abcdefghijklmnopqrstuvwxyyz"))
