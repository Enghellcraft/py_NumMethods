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