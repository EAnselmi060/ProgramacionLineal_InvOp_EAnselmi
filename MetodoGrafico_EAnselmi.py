#Ednoweri Anselmi - CI: 26.355.060 - E.P METODO GRAFICO 
#Librerias necesarias para Metodo Grafico
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
Arr1 = np.array([[1,0],[0,1],[-3,-4]])
Arr2 = np.array([20,10,12])
x1_rango = (0,None)
x2_rango = (0,None)

#Lineas Grafica - restricciones
x1 = np.linspace(0, 60, 10000)
#plt.plot(x1, (x1), label='x <= 20')
plt.axvline(20, 0, 60, label='x <=10', color ='green')
plt.plot(x1, (10 - 0*x1)/1, label='y <= 10')
plt.plot(x1, (12 - 3*x1)/4, label='3x + 4y >= 12')

#Colores Region factible
plt.fill_between(x1, 10, where=((x1) <= 20) & (x1 >= 0), alpha=0.1, color='green')
#plt.fill_between(x1, 0 , (10 - 0*x1)/1, where=((10 - 0*x1)/1 >= 0) & (x1 >= 0), alpha=0.1)
plt.fill_between(x1, 0 , (12 - 3*x1)/4, where=((12 - 3*x1)/4 >= 0) & (x1 >= 0), color='white')

plt.xlim(x1_rango)
plt.ylim(x2_rango)
plt.legend()

#Funcion objetivo y vertice optimo
c = np.array([-5,-6])
resultado = linprog (c, A_ub=Arr1, b_ub=Arr2, bounds=(x1_rango,x2_rango),  method= 'simplex')   


#Punto de la solucion optima en el grafico 
vertice_optim = (resultado.x[0], resultado.x[1])
print(vertice_optim)
plt.plot(vertice_optim[0], vertice_optim[1], 'ro', markersize = 10)
plt.show()
