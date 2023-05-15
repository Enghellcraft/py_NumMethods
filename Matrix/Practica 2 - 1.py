import numpy as np

# creates matrices 3*3 numbers 0 to 9
#for comb in itertools.product(range(10), repeat=9):
# matrix = [[column for column in range(4)] for row in range(4)]

# allows you to enter a matrix manually
""" Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):   
    a = []
    # A for loop for column entries
    for column in range(Column):  
        a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print() """

# a)
def my_matrix_inverse(x):
    try:
        inverse = np.linalg.inv(x)
        # checks if invese is possible
    except np.linalg.LinAlgError:
        print("La matriz no es inversible.")
        pass
    else:
        print("La matriz es inversible.")
        print("La inversa de la matriz es: \n", inverse)
        
# Determinant of a square matrix this can be used instead of the check error
# If the determinant of the matrix is zero, then the matrix has no inverse
def my_determinant(A):
    Aa = np.array(A)
    det = np.linalg.det(Aa)  
    if det == 0:
        return False
    else: 
        return True

matrixA = np.matrix([[1, 0],
                    [2, 1]])

my_matrix_inverse(matrixA)

# b) Ax = B
#    x = A**-1 * B
def my_linear_solution(A, B):
    solution = np.linalg.solve(A, B)
    print("La solución es: \n", solution)
    
matrixB = np.matrix([[3],
                    [4]])

my_linear_solution(matrixA, matrixB)

# c)
matrixC = np.matrix([[1, 1, 0],
                     [0, 1, 0],
                     [0, 1, 1]])

matrixD = np.matrix([[0], 
                     [2],
                     [2]])

my_linear_solution(matrixC, matrixD)

# These are calculator methods, two other method could be: https://www.wikihow.com/Find-the-Inverse-of-a-3x3-Matrix
# a) Transpose the matrix: (practical but takes a lot of time in larger matrices)
#    I)  Check the determinant of the matrix, needs to be different than zero
#   II)  Transpose the original matrix. 
#  III)  Find the determinant of each of the 2x2 minor matrices.   
#   IV)  Create the matrix of cofactors. Place the results of the previous step into a new matrix of cofactors 
#        by aligning each minor matrix determinant with the corresponding position in the original matrix.
#        When assigning signs, the first element of the first row keeps its original sign. The second element is reversed. 
#        The third element keeps its original sign. Continue on with the rest of the matrix in this fashion. Note that the 
#        (+) or (-) signs in the checkerboard diagram do not suggest that the final term should be positive or negative. 
#        They are indicators of keeping (+) or reversing (-) whatever sign the number originally had.
#    V)  Divide each term of the adjugate matrix by the determinant 
#
# b) Using Linear Row Reduction to Find the Inverse Matrix: (powerful for any kind o matrix but not for humans)
#    I) Adjoin the identity matrix to the original matrix. 
#   II) Perform linear row reduction operations. Your objective is to create the identity matrix on the left side of this 
#       newly augmented matrix.
