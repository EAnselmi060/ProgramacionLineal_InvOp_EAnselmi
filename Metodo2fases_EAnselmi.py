#Ednoweri Anselmi - CI: 26.355.060 - E.P METODO 2 FASES
#Librerias necesarias para Metodo 2 fases
from scipy.optimize import linprog

#Definir coeficientes de la funcion objetivo
c = [5,6]

#Definir coeficientes de las restricciones
A = [[1,2],[3,2]]
b = [4,8]

#Definir coeficientes de las variables adiccionales y de holgura
c_fase1 = [0,0,1,1,0,0]
A_fase1 = [[1,2,1,0,1,0], [3,2,0,1,0,1]]
b_fase1 = [4,8]
#Resolver fase 1
res_fase1 = linprog(c=c_fase1, A_ub=A_fase1, b_ub=b_fase1, method="simplex")
#Verificar si existe solucion optima en la fase 1
if res_fase1.success:
    #verificar si la solucion es factible para el problema original
    if res_fase1.fun == 0:
        #Eliminar las variables adicionales y de holgura 
        c_fase2 = c
        A_fase2 = A
        b_fase2 = b

        #Resolver la fase 2
        res_fase2 = linprog(c=c_fase2, A_ub=A_fase2, b_ub=b_fase2, method="simplex")
        #Imprimir Solucion optima fase 2
        print("Se encontro una solucion optima: ")
        print(f"X = {res_fase2.x[0]}, Y = {res_fase2.x[1]}, Z = {res_fase2.fun}")
    else:
        print("El problema no tiene solucion factible")
else:
    print("El problema no tiene solucion optima para la Fase 1")