#! /usr/bin/env python3

# initializing matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# initializing final sum matrix
sum_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i1, j1, i2, j2 = len(matrix1), len(matrix1[0]), len(matrix2), len(matrix2[0]) 

# cheching if the rows and columns of both matrices are same
if (i1 == i2 and j1 == j2):
    # if same then finding sum
    for i in range(0, i1):
        for j in range(0, j1):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print(f"The sum of matrixes are: {sum_matrix}")

else:
    # if not then show error
    print("Error...\nNext time enter the matrix with same number of rows and columns\nExiting... ")