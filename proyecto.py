



class ZeroDivException(Exception):
    def __init__(self, line):
        super().__init__()
        self.line = line

# intermbiar la fila i con la siguiente a menos que que la fila i sea 
# la última; en este caso, se intercambiará con la anterior
def intercambiar_fila(i, arr):
    n = len(arr)
    i_t = arr[i]
    t = 0
    if  n == i:
        t =arr[i-1]
    else:    
        t =arr[i+1]

    arr[i] = t
    arr[i+1] = i_t


    return (arr, 1)


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
       # print("i={0} x={1} suma={2}".format(i, x, suma))

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


print(x)

