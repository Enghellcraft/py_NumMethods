import numpy as np
import scipy
import scipy.linalg as linalg 

# LU method
def my_lu(A):
    if my_zero_on_diagonal(A) == False:
        return print("Algun Elemento en la diagonal es 0 y no puede resolverse")
    else:
        if my_square_matrix(A) == False:
            print("La matriz debe ser una matriz cuadrada")
        else:
            if my_determinant() == False:
                print("La determinante debe ser distinta a cero")
            else:        
                print ("Solutions: se pueden solucionar los elementos de la matriz")

# Zero on Diagonal
def my_zero_on_diagonal(A):
    for i in range(0,len(A) ) :
        print(A[i][i])
        if (A[i][i] == 0) :
            return False
    return True

# Square Matrix
def my_square_matrix(A):
    if len(A) != len(A[0]) and len(set(map(len, A))) != 1:
        return False
    else:
        return True

# Determinant of a square matrix
def my_determinant(A):
    Aa = np.array(A)
    det = np.linalg.det(Aa)  
    if det == 0:
        return False
    else: 
        return True

# Permutation Matrix
def my_permutation(A):
    P, L, U = scipy.linalg.lu(A)
    print("La matriz de permutacion es: \n")
    print(P)
    print(L)
    print(U)
    
# Data
matrixA = ([[1,1],
            [0,0]])

matrixB = ([[2,1],
            [6,3]])

matrixC = ([[1,2],
            [3,4]])

matrixD = ([[1,0,1],
            [0,1,0],
            [1,1,1]])

matrixE = ([[1,2,3],
            [0,0,2],
            [2,2,3]])

my_lu(matrixA)
my_lu(matrixB)
my_lu(matrixC)
my_lu(matrixD)
my_lu(matrixE)
