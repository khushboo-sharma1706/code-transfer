"""Write a Python program to print the alphabet pattern 'X'.
Expected Output:
*     *
 *   *
  * *
   *
  * *
 *   *
*     *"""

for i in range(3, 0, -1):
    print(f"{' ' * (3 - i)}*{' ' * ((i * 2) - 1)}*")
print("   *")
for i in range(1, 4):
    print(f"{' ' * (3 - i)}*{' ' * ((i * 2) - 1)}*")


for i in range(3, 0, -1):
    print(' ' *(3 - i), end="")
    print("*", end="")
    print(' '*((i*2)-1), end="")
    print("*", end="")
    print("")
print("   *")
for i in range(1, 4):
    print(' ' * (3 - i), end="")
    print("*", end="")
    print(' ' * ((i * 2) - 1), end="")
    print("*", end="")
    print("")
