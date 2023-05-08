# Tanto el método de Lagrange como el de Newton son técnicas utilizadas en cálculo
# para aproximar una función desconocida a partir de un conjunto finito de puntos
# conocidos. El método de Lagrange se utiliza para la interpolación de datos y el 
# de Newton se utiliza para la interpolación y extrapolación de datos.

#El método de Lagrange utiliza una fórmula de interpolación que se basa en las 
# ordenadas de una función y no en las diferencias divididas como lo hace el método
# de Newton [2]. El método de Lagrange se utiliza para encontrar una función que 
# pase por un conjunto de puntos conocidos de una manera suave y continua.
# Para encontrar esta función, se utiliza una función polinómica que pasa por 
# cada uno de los puntos conocidos. La fórmula de interpolación de Lagrange se 
# puede escribir como:
#Pn(x)=∑i=0nyiLi(x)

#Donde Pn(x) es la función polinómica que se ajusta a los puntos conocidos, yi es la
# ordenada correspondiente al punto xi, y Li(x) es la función de Lagrange, definida 
# como:
#Li(x)=∏j=0,j≠inx−xjxi−xj

#La ventaja del método de Lagrange es que es fácil de entender y aplicar. Sin embargo,
# su principal limitación es que no es eficiente para grandes conjuntos de datos [2].

#Por otro lado, el método de Newton utiliza un polinomio interpolante que se escribe
# como una suma de términos que involucran las diferencias divididas de los puntos 
# conocidos. El polinomio interpolante de Newton se puede escribir como:
#Pn(x)=f[x0]+f[x0,x1](x−x0)+f[x0,x1,x2](x−x0)(x−x1)+⋯+f[x0,x1,…,xn](x−x0)(x−x1)⋯(x−xn−1)

#Donde f[x0,x1,…,xn] es la diferencia dividida de orden n y f[xi] es la función 
# evaluada en el punto xi [3].

#La ventaja del método de Newton es que es más eficiente que el método de Lagrange 
# para grandes conjuntos de datos. Además, el método de Newton se puede utilizar 
# para la interpolación y extrapolación de datos, mientras que el método de Lagrange 
# solo se utiliza para la interpolación [3].

#Ambos métodos generalizan la propiedad euclidiana de que por dos puntos distintos
# pasa siempre una (única) recta, ya que permiten encontrar una función polinómica 
# que pase por un conjunto de puntos conocidos de una manera suave y continua. Sin 
# embargo, cada método tiene sus ventajas y desventajas, y el método que se elige 
# dependerá del conjunto de datos que se esté analizando.

#En resumen, el método de Lagrange se utiliza para la interpolación de datos y se
# basa en una fórmula de interpolación que se basa en las ordenadas de una función,
# mientras que el método de Newton se utiliza para la interpolación y extrapolación
# de datos y se basa en un polinomio interpolante que se escribe como una suma de
# términos que involucran las diferencias divididas de los puntos conocidos. Ambos 
# métodos permiten encontrar una función polinómica que pase por un conjunto de puntos
# conocidos de una manera suave y continua, generalizando la propiedad euclidiana de
# que por dos puntos distintos pasa siempre una (única) recta.