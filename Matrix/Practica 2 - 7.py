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

    D = np.diag(np.diag(coefficient_matrix))
    L = np.tril(coefficient_matrix, k=-1)
    U = np.triu(coefficient_matrix, k=1)
    
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

coefficient = np.array([[2, -1, 1], [1, 3, 1], [1, 1, 9]])
constant = np.array([[-1], [0], [4]])
init_val = [0, 0, 0]
iterations = 2
print (f"""{jacobi_iteration_method(coefficient, constant, init_val, iterations)}""")







"""# Ingrese el número de variables independientes mu, el número de ecuaciones nu, la precisión del error de iteración e
a = input("Introduzca el número mu de la variable independiente X y el número nu de la ecuación:")
mu, nu = [int(i) for i in a.split(" ")]
b = input("Ingrese la precisión de error requerida e:")
e = float(b)
print(str(mu) + "  " + str(nu)+" "+str(e))

# Inicializar la matriz LDU (p es el número de filas, q es el número actual de columnas)
L, D, U = [], [], []  # Inicializar la matriz LDU
for p in range(nu):
    L.append([]), D.append([]), U.append([])
    for q in range(mu):
        x_in = float(input("Introduzca el coeficiente en la fila% dy la columna% d:" % (p + 1, q + 1)))
        if p < q:
            L[p].append(x_in), D[p].append(0), U[p].append(0)
        elif p == q:
            L[p].append(0), D[p].append(x_in), U[p].append(0)
        else:
            L[p].append(0), D[p].append(0), U[p].append(x_in)
L, D, U = np.array(L), np.array(D), np.array(U)

# Construyendo el valor inicial X_Matriz actual de la variable independiente
X_Current = []  # Variable independiente x matriz
for q in range(mu):
    x_in = float(input("Introduzca el valor inicial de X% d:" %q))
    X_Current.append(x_in)
X_Current = np.array(X_Current).T  # Transponer el vector de fila X a un vector de columna para facilitar el cálculo de la matriz subsiguiente;

# Inicializar la matriz de variable dependiente y
b_Const = []  # Matriz y variable dependiente
for p in range(nu):
    y_in = float(input("Introduzca el valor Y de la ecuación% d:" % (p + 1)))
    b_Const.append(y_in)
b_Const = np.array(b_Const).T  # Transponer el vector de fila X a un vector de columna para facilitar el cálculo de la matriz subsiguiente;

# Calcule y obtenga la matriz G1, d1 (consulte la fórmula de iteración de Jacobi anterior)
L_U = copy.deepcopy(L)
for p in range(nu):
    for q in range(mu):
        L_U[p][q] = L[p][q]+U[p][q]  # Suma L y U por fila y suma las posiciones correspondientes
        
G1 = np.dot(-np.linalg.inv(D), L_U)  # np.linalg.inv (D) Encuentre la inversa de la matriz
d1 = np.dot(np.linalg.inv(D), b_Const)

# Ponga la fórmula de cálculo iterativo en el ciclo, cuando el error de iteración alcance la precisión de e, imprima el resultado de la solución de X
# x^(k+1) = G1*x^(k) + d1
X_New = copy.deepcopy(X_Current)  # Importar la biblioteca de copias, copia profunda X_Current como inicialización de X_New;

# Iteración de Jacobi
epoch = 0  # Número de iteraciones
while 1:
    flag = 0  # Marca de precisión de error, cuente el número de x que cumplen con los requisitos de precisión, cuando todos los resultados de x iteraciones en la misma época de X_New alcanzan la precisión, salida X_New
    X_Current = X_New
    X_New = np.dot(G1, X_Current)
    for p in range(mu):
        X_New[p] = X_New[p] + d1[p]
        if math.fabs(X_New[p]-X_Current[p]) < e:
            flag += 1
    epoch += 1
    if epoch > 50:  # De acuerdo con las características de convergencia de la iteración de Jacobi, establezca el límite superior de iteración en 50 veces;
        print("¡La iteración de Jacobi no converge!")
        epoch = 0
        break

    if flag == mu:
        print("Los resultados de la iteración de Jacobi son los siguientes:")
        print(X_New)
        break

# flag == mu, # Marca de precisión de error, cuente el número de x que cumplen con los requisitos de precisión, cuando todos los resultados de x iteraciones en la misma época de X_New alcanzan la precisión, salida X_New. 2. época> 50, 
"""


# Gauss
# Calcular L + U
""" D_L = copy.deepcopy(L)
for p in range(mu):
    for q in range(nu):
        D_L[p][q] = D[p][q]+L[p][q]

G2 = np.dot(-np.linalg.inv(D_L), U)  # np.linalg.inv (D + L) Halla la inversa de la matriz
d2 = np.dot(np.linalg.inv(D_L), b_Const)
 """