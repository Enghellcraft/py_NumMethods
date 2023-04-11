import numpy as np
from numpy import float64
from numpy.typing import NDArray
import scipy.linalg as la

# Method to find solution of system of linear equations
def jacobi_iteration_method(
    coefficient_matrix: NDArray[float64],
    constant_matrix: NDArray[float64],
    init_val: list[int],
    iterations: int,
) -> list[float]:
    
    rows1, cols1 = coefficient_matrix.shape
    rows2, cols2 = constant_matrix.shape

    if rows1 != cols1:
        print(f"Coefficient matrix dimensions must be nxn but received {rows1}x{cols1}")

    if cols2 != 1:
        print(f"Constant matrix must be nx1 but received {rows2}x{cols2}")

    if rows1 != rows2:
        print(
            f"""Coefficient and constant matrices dimensions must be nxn and nx1 but
            received {rows1}x{cols1} and {rows2}x{cols2}"""
        )

    if len(init_val) != rows1:
        print(
            f"""Number of initial values must be equal to number of rows in coefficient
            matrix but received {len(init_val)} and {rows1}"""
        )

    if iterations <= 0:
        print("Iterations must be at least 1")

    table: NDArray[float64] = np.concatenate(
        (coefficient_matrix, constant_matrix), axis=1
    )

    rows, cols = table.shape

    strictly_diagonally_dominant(table)

    # Iterates the whole matrix for given number of times
    for _ in range(iterations):
        new_val = []
        for row in range(rows):
            temp = 0
            for col in range(cols):
                if col == row:
                    denom = table[row][col]
                elif col == cols - 1:
                    val = table[row][col]
                else:
                    temp += (-1) * table[row][col] * init_val[col]
            temp = (temp + val) / denom
            new_val.append(temp)
        init_val = new_val

    L, D, U = [], [], []  # Inicializar la matriz LDU
    (P, L, U) = la.lu(coefficient_matrix)
    D =  np.diag(np.diag(U))
    
    result = [float(i) for i in new_val]
    return print("El resultado, luego de ", iterations, " iteraciones, es: ", result,"\n La matriz L: \n", L,"\n La matriz D: \n", D,"\n La matriz U: \n", U,"\n")

# Checks if the given matrix is strictly diagonally dominant
def strictly_diagonally_dominant(table: NDArray[float64]) -> bool:

    rows, cols = table.shape

    is_diagonally_dominant = True

    for i in range(0, rows):
        total = 0
        for j in range(0, cols - 1):
            if i == j:
                continue
            else:
                total += table[i][j]

        if table[i][i] <= total:
            print("Coefficient matrix is not strictly diagonally dominant")
            break

    return is_diagonally_dominant

coefficient = np.array([[4, 1, 1], [1, 5, 2]])
constant = np.array([[-1], [0], [4]])
init_val = [0, 0, 0]
iterations = 3
print (f"""{jacobi_iteration_method(coefficient, constant, init_val, iterations)}""")