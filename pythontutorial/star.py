"""*
   **
   ***
   ****
   *****"""
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

print("")
for i in range(4,-1,-1):
    for j in range(i+1):
        print("*",end="")
    print()

print("")
#space = 4
for i in range(5):
    for j in range(5-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()
    #space = space-1

print("")
#space = 4
for i in range(5):
    for j in range(5-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print()
    #space = space-1


print("")
k = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(k, end=" ")
        k = k + 1
    print()

print("")
k = 65
for i in range(4,-1,-1):
    for j in range(0, i+1):
        print(chr(k), end=" ")
        k = k + 1
    print()

print()
print(ord("b"))
print()
print(chr(70))
print()


for i in range(5):
        if i == 4:
            for j in range(i+1):
                print("*", end="")
                continue
        print("*", end="")
        print()

