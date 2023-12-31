"""Write a Python program that takes two digits m (row) and n (column) as input and generates a
two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1

Sample:
Input number of rows: 3
Input number of columns: 4
[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]"""

"""m=int(input("Row:"))
n=int(input("Column:"))
matrix=[[0 for col in range(n)] for row in range(m)]
for row in range(m):
    for col in range(n):
        matrix[row][col]=row*col
print(matrix)"""

m = int(input("Number of Rows: "))
n = int(input("Number of Columns: "))
matrix =[[0 for col in range(n)] for row in range(m)]
for row in range(m):
    for col in range(n):
        matrix[row][col]=row*col
print(matrix)
