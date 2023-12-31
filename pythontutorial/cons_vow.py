def cons_vow(n):
    if n in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return "Vowel"
    else:
        return "Consonant"

a = (input("Enter Alphabet : "))
print(f"{a} is {cons_vow(a)}",)
