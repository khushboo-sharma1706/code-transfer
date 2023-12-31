"""Create a class called 'Matrix' containing constructor that initializes the number of rows
 and the number of columns of a new Matrix object. The Matrix class has the following information:
1 - number of rows of matrix
2 - number of columns of matrix
3 - elements of matrix (You can use 2D vector)
The Matrix class has functions for each of the following:
1 - get the number of rows
2 - get the number of columns
3 - set the elements of the matrix at a given position (i,j)
4 - adding two matrices.
5 - multiplying the two matrices
6 - reset the matrix to have all the values to "0"
7 - change the row count of matrix, only allow increment
You can assume that the dimensions are correct for the multiplication and addition."""


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.elements = [[0 for i in range(row)] for j in range(column)]

    def get_rows(self):
        return self.row

    def set_rows(self, row):
        self.row = row

    def get_columns(self):
        return self.column

    def set_element(self, row, column, value):
        self.elements[row][column] = value

    def add_matrix(self, second_matrix):
        r = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                value = self.elements[i][j] + second_matrix.elements[i][j]
                r.set_element(i, j, value)
        return r

    def multi_matrix(self, second_matrix):
        r = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                value = 0
                for k in range(self.row):
                    value += self.elements[i][k] * second_matrix.elements[k][j]
                r.set_element(i, j, value)
        return r

    def reset_matrix(self):
        self.elements = [[0 for i in range(self.row)] for j in range(self.column)]

    def increase_row_count(self, row):
        iv = row-self.row  #2
        for i in range(iv):
            self.elements.append([0 for i in range(self.column)])
# 1 2 3      1 1 1      0 0 0
# 4 5 6   +  1 1 1   =  0 0 0
# 7 8 9      1 1 1      0 0 0
# 0 0 0
# 0 0 0


# (00*00)+(01*10)+(02*20)
# (00*01)+(01*11)+(02*21)   (ik*kj)+
m1 = Matrix(3, 3)
m2 = Matrix(3, 3)
count = 1
for i in range(3):
    for j in range(3):
        m1.set_element(i, j, count)
        m2.set_element(i,j,1)
        count+= 1

result = m1.add_matrix(m2)
result2 = m1.multi_matrix(m2)
print(result.elements)
print(result2.elements)
# m1.reset_matrix()
print(m1.elements)
m1.increase_row_count(10)
print(m1.elements)

print("Sorrryy Wifeyyy!!!!!")