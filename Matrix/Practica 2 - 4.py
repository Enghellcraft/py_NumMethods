import numpy as np
import scipy
import scipy.linalg as linalg 

# LU method
def my_lu(A, B, N):
    if my_zero_on_diagonal(A, N) == False:
        return print("Algun Elemento en la diagonal es 0 y no puede resolverse")
    else:
        LU = linalg.lu_factor(A) 
        x = linalg.lu_solve(LU, B) 
        print ("La solucion es:\n",x )

# Zero on Diagonal
def my_zero_on_diagonal(A, N):
    for i in range(0,N-1) :
        if (A[i][i] == 0) :
            return False
    return True


# Permutation Matrix
def my_permutation(A):
    P, L, U = scipy.linalg.lu(A)
    print("La matriz de permutacion es: \n")
    print(P)
    print(L)
    print(U)

# Inverts a matrix
def my_inverse(A):
    Am = np.matrix(A)
     # Check shape of A
    if (Am.shape[0] != Am.shape[1]):
        print("La matriz no es cuadrada")
        return
    
    Aa = np.array(A)
    if np.linalg.det(Am) == 0:
        return print("No es inversible")
    else:
        #adj(Aa)/det(Aa)
        Ainv = np.linalg.inv(Am)
        print("La matriz inversa es: \n", Ainv)
        
# Data
matrixC = np.array([[1, 1, 0],
                     [0, 1, 0],
                     [0, 1, 1]])

matrixD = np.array([[0], 
                     [2],
                     [2]])

my_lu(matrixC, matrixD, 3)
my_permutation(matrixC)
my_inverse(matrixC)
