""" Problema:
 Escribir un programa que reciba n y un sistema de n ecuaciones con n 
 variables, y que regrese la solución del sistema.
"""


""" 
 En esta primera parte vamos a ver múltiples formas de representar, a través 
 de un diccionario, el sistema de ecuaciones:
 
    2a + 2b = 2
    5a + 5b = 5
    
"""

sistema_por_variables={}

variables=["a", "b"]
valores=[2, 5]


for n in variables:
    sistema_por_variables[n] = list(valores)



sistema_por_variables["c"] = list(valores)
print(sistema_por_variables)

#####################################################################
sistema_por_ecuaciones={}
ecuaciones = ["primera", "segunda"]
valores = [2, 5]
resultados = [2, 5]

# Al parecer al utilizar el operador '=' pasamos el puntero, no los valores ...
for n in ecuaciones:
    # por eso es necesario hacer una copia explícita
    sistema_por_ecuaciones[n] = list(valores)


for i in range(len(ecuaciones)):
    sistema_por_ecuaciones[ecuaciones[i]].append(resultados[i])
 

print(sistema_por_ecuaciones)
