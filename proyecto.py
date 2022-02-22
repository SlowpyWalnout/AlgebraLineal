"""
    Escribir un programa que reciba n y un sistema de n ecuaciones con n variables,
    y que regrese la solución del sistema.
"""

class ZeroDivException(Exception):
    def __init__(self, line):
        super().__init__()
        self.line = line

# intercambiar la fila i con la siguiente a menos que que la fila i sea 
# la última; en este caso, se intercambiará con la anterior
def intercambiar_fila(i, matriz):
    n = len(matriz)
    fila = matriz[i]
    fila_destino = []
    n_fila_destino = 0
    if  n == i:
        n_fila_destino = i-1
        fila_destino = matriz[n_fila_destino]
    else:    
        n_fila_destino = i+1
        fila_destino = matriz[n_fila_destino]

    matriz[i] = fila_destino
    matriz[n_fila_destino] = fila


# donde matriz es una lista de dos dimensiones con las filas de la matriz
# y n = len(matriz)
def dividir_por_diagonal(matriz, n):
    # recorremos las columnas, porque estamos incluyendo los resultados
    for j in range(0,n+1):
        # recorremos las filas
        for i in range(0, n):
            # Dejamos intacta la fila superior
            if i>j:
                # Dividir la posición de la matriz por la diagonal anterior
                divisor = matriz[j][j]

                if divisor == 0:
                    raise ZeroDivException(j)

                division=matriz[i][j]/divisor
                
                # Recorremos de las columnas de la fila actual
                for k in range(0, n+1):
                    # Restamos a cada posición de la fila
                    matriz[i][k]=matriz[i][k]-division*matriz[j][k];

                
# Generamos un "vector" vacío con longitud n
def generar_x(n):
    x = []
    for _ in range(0, n):
        x.append(0)
    return x


def obtener_vector_resultados(matriz, n, x):
    # Recorremos las columnas en orden inverso
    for i in range(n,0,-1):
        suma=0
                
    #Recorre las...
        for j in range(i,n):
            suma=suma+matriz[i-1][j]*x[j]

        #Insertar las respuestas en x
        dividendo = matriz[i-1][i-1]
        if dividendo == 0:
            raise ZeroDivException(i-1)
        
        x[i-1]=((matriz[i-1][n]-suma)/dividendo)	

########################### PRUEBAS ###############################
"""
matriz = [[3,2,3,3,10], [3,2,1,-6,2], [5,1,3,12,6], [-4,-4,8,1,5]]
matriz = [[3,2,3,3,10], [5,1,3,12,6], [3,2,1,-6,2], [-4,-4,8,1,5]]
"""

matriz = [[3, 2, -6, 5, -6, 2], [3, 2, -2, 15, 5, 5], [3, 1, -1, -2, 1, 7], [5, -9, -6, 20, 1, 10], [8, 1, -15, 4, 2, 0]]
n = len(matriz)
try:
    dividir_por_diagonal(matriz, n)
except ZeroDivException as err:
    print("exepcion encontrada")
    linea_error = err.line
    intercambiar_fila(linea_error, matriz)
    dividir_por_diagonal(matriz, n)

x = generar_x(n)
try:
    obtener_vector_resultados(matriz, n, x)
except ZeroDivException as err:
    linea_error = err.line
    intercambiar_fila(linea_error, matriz)
    obtener_vector_resultados(matriz, n, x)


for i in range(0,n):
	print("x_"+str(i+1)+" = "+str(x[i]))

