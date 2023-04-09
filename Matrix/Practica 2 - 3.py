import numpy as np

# Norm2 of a matrix
def my_norm2(A):
    norm= np.linalg.norm(A, ord = 1, axis=1,keepdims=True )

    return print("La norma 2 de la Matriz es: \n", norm)

#Data
mat = np.array([[3, 3],
       [3, 3]])

my_norm2(mat)