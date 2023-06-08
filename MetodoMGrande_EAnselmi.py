#Ednoweri Anselmi - CI: 26.355.060 - E.P METODO M GRANDE 
#Librerias necesarias para Metodo M Grande
from scipy.optimize import minimize

#Definir La funcion objetivo y las Restricciones
def funcion_objetivo(x):
    return 5 * x[0] + 6 * x[1]

def rest_1(x):
    return 4 - .5 * x[0] - .20 * x[1] 

def rest_2(x):
    return 20 - 2 * x[0] - 3 * x[1]

def rest_3(x):
    return 10 - x[0] - x[1] 

#Definir el valor de M 
M=1000

#Definir la funcion de restriccion con variables artificiales
def funcion_restriccion(x):
    return [rest_1(x), rest_2(x), rest_3(x), M * max(0, -rest_1(x)), M * max(0, -rest_2(x)), M * max(0, -rest_3(x))]

#Definir punto de partida para la optimizacion
x0 = [0,0]

#Resolver metodo a traves de la funcion minimize
resultado = minimize(funcion_objetivo, x0, method='SLSQP', constraints=({'fun': funcion_restriccion, 'type': 'ineq'}))

#Imprimir el resultado
if resultado.success:
    print("Solucion optima: ")
    print("x = ",round(resultado.x[0],2))
    print("y = ",round(resultado.x[1],2))
    print("El valor optimo de la funcion objetivo: Z = ", round(-resultado.fun, 2))
else:
    print("El problema no tiene solucion optima.")