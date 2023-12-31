"""Write a Python program that accepts a comma-separated sequence of words as input and
prints the distinct words"""

a = "Khushboo,Sharma,Gauri,Yogita"
list1 = []
c = 0
for i in range(len(a)):
    if a[i] == ",":
        list1.append(a[c:i])
        c = i+1
        print(list1)
list1.append(a[c:])
print(list1)



