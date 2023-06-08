#Ednoweri Anselmi - CI: 26.355.060 - E.P METODO SIMPLEX 
#Librerias necesarias para Metodo Simplex
import numpy as np
from scipy.optimize import linprog

#Definir la funcion objetivo
c = np.array([5,6])
A = np.array([[4,6],[20,10]])
b = np.array([480,1500])

#Resolver simplex a traves de la funcion linprog
resultado = linprog (-c, A_ub=A, b_ub=b, method= 'simplex')  

#Imprimir el resultado
print("Status: ", resultado.message)
print("Solucion optima: ")
print("x = ",round(resultado.x[0],2))
print("y = ",round(resultado.x[1],2))
print("El valor optimo de la funcion objetivo: Z = ", round(-resultado.fun, 2))