import numpy as np
from sympy import det

# Fills transpose of mat[N][N] in tr[N][N]
def my_transpose(mat,tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
            
# Returns if mat[N][N] is symmetric
def my_isSymmetric(mat, N):
    tr = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    my_transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return print("No es Simetrica")
    return print("Es Simetrica")

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
    

# Sums two matrices
def my_sum(A, B):
    return np.array(A) + np.array(B)

# Substraction between two matrices
def my_subs(A, B):
    return np.array(A) - np.array(B)

# Multiplication between two matrices
def my_mul(A, B):
    return np.array(A) * np.array(B)

# Compare two matrices
def my_compare(A, B):
    Aa = np.array(A)
    Ba = np.array(B)
    if np.array_equal(Aa, Ba):
        return print("Matrices son iguales")
    else:
        return print("Matrices no son iguales")

# Times two matrix
def my_times(A):
    return np.array(A)**2

# Datasets
symMatrixA =         ([[7, 2, 0],
                      [2, 1, 1],
                      [0, 1, 3]])

symMatrixB =        ([[1, 5, 3],
                      [5, 2, 1],
                      [3, 1, 1]])

unsymMatrixA =         ([[7, 2, 0],
                      [2, 1, 1],
                      [5, 1, 3]])

simMatrixE = ([[1, 3],
                [1, 5]])

simMatrixEp = ([[1, 0],
                [0, 1]])

print("Matriz A: \n", symMatrixA)
my_isSymmetric(symMatrixA, 3)
print("Matriz B: \n", symMatrixB)
my_isSymmetric(symMatrixB, 3)



# a)
print("A: ")
print("Matriz A simetrica: \n", symMatrixA)
my_isSymmetric(symMatrixA, 3)
print("Matriz B simetrica: \n", symMatrixB)
my_isSymmetric(symMatrixB, 3)
symMatrixC = my_sum(symMatrixA, symMatrixB)
print("Matriz C (matriz A + matriz B):\n", symMatrixC)
my_isSymmetric(symMatrixC, 3)
print("_________________________________________________")

#b) Simetricas y no simetricas dan una matriz suma simetrica
print("B: ")
print("Matriz A no simetrica: \n", unsymMatrixA)
my_isSymmetric(unsymMatrixA, 3)

unsymMatrixAT = np.transpose(unsymMatrixA)
print("Matriz A**t: \n", unsymMatrixAT)
my_isSymmetric(unsymMatrixAT, 3)

symMatrixD = my_sum(unsymMatrixA, unsymMatrixAT)
print("Matriz D (matriz A + matriz A**t):\n", symMatrixD)
my_isSymmetric(symMatrixD, 3)
# -------------------------------------------------
print("Matriz A simetrica: \n", symMatrixA)
my_isSymmetric(symMatrixA, 3)

symMatrixAT = np.transpose(symMatrixA)
print("Matriz A**t: \n", symMatrixAT)
my_isSymmetric(symMatrixAT, 3)

symMatrixD = my_sum(symMatrixA, symMatrixAT)
print("Matriz D (matriz A + matriz A**t):\n", symMatrixD)
my_isSymmetric(symMatrixD, 3)
print("_________________________________________________")

#c) Solo matrices antisimetricas porque en matrices simetricas A = A^t. 
print("C: ")
not_unsymMatrixA = my_subs(symMatrixA, symMatrixAT)
print("Matriz Simetrica A (matriz A - matriz A**t):\n", not_unsymMatrixA)
my_isSymmetric(not_unsymMatrixA, 3)

unsymMatrixA = my_subs(unsymMatrixA, unsymMatrixAT)
print("Matriz Asimetrica A (matriz A - matriz A**t):\n", unsymMatrixA)
my_isSymmetric(unsymMatrixA, 3)
print("_________________________________________________")

#d) 
print("D: ")
not_unsymMatrixA = my_mul(symMatrixA, symMatrixAT)
print("Matriz Simetrica A (matriz A * matriz A**t):\n", not_unsymMatrixA)
my_isSymmetric(not_unsymMatrixA, 3)

unsymMatrixA = my_mul(unsymMatrixA, unsymMatrixAT)
print("Matriz Asimetrica A (matriz A * matriz A**t):\n", unsymMatrixA)
my_isSymmetric(unsymMatrixA, 3)
print("_________________________________________________")

#e) solo cuando toma matriz identidad
print("E: ")
print("Matriz E simetrica: \n", simMatrixE)
my_isSymmetric(simMatrixE, 2)

simMatrixEinv = my_inverse(simMatrixE)

my_compare(simMatrixE, simMatrixEinv)

simMatrixET = np.transpose(simMatrixE)
timesTwoMatrixET = my_times(simMatrixET)
print("Matriz (E**t )**2: \n", timesTwoMatrixET)

#------------------------------------------------
print("Matriz Ep simetrica: \n", simMatrixEp)
my_isSymmetric(simMatrixEp, 2)

simMatrixEpinv = my_inverse(simMatrixEp)

my_compare(simMatrixEp, simMatrixEpinv)

simMatrixEpT = np.transpose(simMatrixEp)
timesTwoMatrixEpT = my_times(simMatrixEpT)
print("Matriz (E**t )**2: \n", timesTwoMatrixEpT)


print("_________________________________________________")