"""Q1: Write a Python program to append a new item to the end of the array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])"""

a = ["i", [1, 3, 5, 7, 9]]
a[1].append(11)
print(a)
print("List is : " + str(a))
