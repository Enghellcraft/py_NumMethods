import scipy
import scipy.linalg as linalg 
import numpy as np

# LU method
# LU method
def my_lu(A):
    if my_zero_on_diagonal(A) == False:
        return print("Algun Elemento en la diagonal es 0 y no puede resolverse")
    else:
        if my_square_matrix(A) == False:
            print("La matriz debe ser una matriz cuadrada")
        else:
            if my_determinant(A) == False:
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
    P, L, U = linalg.lu(A)
    print("Para la matriz: ")
    print(A)
    print("La matriz de permutacion L y U:")
    print(L)
    print(U)


# Data
matrixA = ([[1,0,0],
            [2,1,0],
            [5,3,1]])

matrixB = ([[1,2,3],
            [0,1,6],
            [0,0,1]])

matrixC = ([[1,0,0],
            [0, 2, 0],
            [0, 0, 3]])
            
            
            
# a)
my_lu(matrixA)
my_permutation(matrixA)
print("Si A es triangular inferior con unos en la diagonal, L es la matriz A y U es la matriz identidad.")
# b)
my_lu(matrixB)
my_permutation(matrixB)
print("Si A es triangular superior con unos en la diagonal, U es la matriz A y L es la matriz identidad.")
# c)
my_lu(matrixC)
my_permutation(matrixC)
print("Si A es diagonal con elementos diagonales no nulos, L es la matriz identidad y U es la matriz A.")