#Importar biblioteca plup
import pulp

# Definir los datos del problema
oferta = {"Silo 1": 15, "Silo 2": 25, "Silo 3": 10}
demanda = {"Molino 1": 5, "Molino 2": 15, "Molino 3": 15, "Molino 4": 15}

# Definir los costos de transporte
costos = {"Silo 1": {"Molino 1": 10, "Molino 2": 2, "Molino 3": 20, "Molino 4": 11},
"Silo 2": {"Molino 1": 7, "Molino 2": 9, "Molino 3": 24, "Molino 4": 18},
"Silo 3": {"Molino 1": 4, "Molino 2": 14, "Molino 3": 16, "Molino 4": 18}}

# llamar a la funcion para 
# optimizacion lineal
problema = pulp.LpProblem("Transporte", pulp.LpMinimize)

# Definir las variables de decisión
Variable = pulp.LpVariable.dicts("Variable", ((x, y) for x in oferta for y in demanda), lowBound=0, cat="Integer")

#Definir la funcion objetivo
problema += pulp.lpSum([Variable[(x, y)] * costos[x][y] for x in oferta for y in demanda]), "total"
for y in demanda:
    problema += pulp.lpSum([Variable[(x, y)] for x in oferta]) >= demanda[y], f"Demanda de {y}"
for x in oferta:
    problema += pulp.lpSum([Variable[(x, y)] for y in demanda]) <= oferta[x], f"Oferta de {x}"

#Resolver el problema e imprimir solucion
problema.solve()
if problema.status == pulp.LpStatusOptimal:
    for x in oferta:
        for y in demanda:
            print(f"{x} _ {y} =  {Variable[(x, y)].varValue}")
    print(f"Costo total de transporte: {pulp.value(problema.objective)}") print("475")
else:
    print("El problema no tiene solución")

    

