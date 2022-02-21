import numpy as np

def swag(a, b):     #Función de matriz de intercambio
    for i in range(0, len(a)):
        t = a[i]
        a[i] = b[i]
        b[i] = t

def print_matrix( info, matrix ):       #Imprimir matriz
    print (info)
    for i in range( 0, matrix.shape[0]):
        print('[', end='')
        for j in range( 0, matrix.shape[1]):
            if(j == matrix.shape[1] - 1):   # Vector b
                print( '|', end=''),                           # Separe la matriz de coeficientes y el vector b con "|"
            print("%5.2f" %matrix[i][j], end=' ')
            if j == matrix.shape[1] - 1:                  # Elemento de matriz de salida m [i] [j]
                print(']', end=' ')
                print('\n')

def check(matrix, i, row, col):         # Función de juicio, utilizada para detectar si los valores de las filas de la matriz procesada actualmente son todos 0, si son todos ceros, luego recorra desde la fila inferior de la matriz para encontrar las filas que no son todas ceros e intercambie con esta fila, y luego intercambie las filas intercambiadas Procesando
    if 0.00 in set(matrix[i]) and len(set(matrix[i])) == 1:     #Determina si la fila actual es todo ceros y agrega la fila actual para ver si solo tiene un elemento 0
        for j in range(row - 1, i ,-1):                         # Encuentra una fila que no sea todo ceros de la última fila de la matriz
            try:
                if not(0.00 in set(matrix[j]) and len(set(matrix[j])) == 1):    #Determina si esta línea es cero
                    swag(matrix[i], matrix[j])                                  #intercambiar
                    select(matrix, i, col)                                      # Intercambiar y luego pisar
                    break
            except:                     # Si el recorrido encuentra que no hay filas que no sean cero, regrese directamente
                return

def select(matrix, i, col):            # Función de procesamiento escalonado #Matrix
    if 0.00 in set(matrix[i]) and len(set(matrix[i])) == 1:     # Principalmente para la última fila de la matriz, la función de juez no puede emitir un juicio distinto de cero en la última fila
        return
    for k in range(0, i):                                       #i es el número de filas de la matriz que se está procesando actualmente, este ciclo es para realizar el procesamiento paso a paso en la fila i-ésima de la matriz
        temp = matrix[i][k] / matrix[k][k]                      # De acuerdo con la matriz pivote [k] [k], determine el divisor de la matriz [i] [k] a cero
        if temp == 0:                                           # El elemento principal es 0 y no se realiza ninguna operación
            continue
        for j in range(0, col):                                 #Opere todos los números en esta fila, y el número en la misma columna que el pivote volverá a cero
            matrix[i][j] = matrix[i][j] - matrix[k][j] * temp

def solve(matrix):                      #La parte principal del algoritmo
    row = matrix.shape[0]                       #Obtener el número de filas de la matriz
    col = matrix.shape[1]                       #Obtener el número de columnas de la matriz
    for i in range(0, row):                     #Compruebe si el pivote de una fila de la matriz es 0, si es cero, recorra para encontrar la fila que no es cero para intercambiar con ella
        if matrix[i][i] == 0:                   #     matriz [i] [i] es el pivote de la i-ésima fila
            for j in range(i + 1, row):
                if matrix[j][i] != 0:
                    swag(matrix[i], matrix[j])
                    break
        select(matrix, i, col)                  # Realizar operación escalonada
        check(matrix, i, row, col)              #Determine si el valor de esta fila se reducirá a cero después del paso, si se reduce a cero, cámbielo por otras filas que no sean cero y luego realice el procesamiento por pasos

def to_one(matrix):                     #Convierta la matriz en la matriz de filas más simple
    row = matrix.shape[0]
    col = matrix.shape[1]
    for i in range(0, row):                         # Todos los pivotes de cada fila de la matriz están normalizados
        temp = matrix[i][i]
        for j in range(i, col):
            matrix[i][j] = matrix[i][j] / temp
    for i in range(0, row - 1):                     # Vuelve a cero para cada fila de la matriz
        for j in range(i + 1, col - 1):             #Comience a atravesar desde el elemento principal hasta cero para cada número
            temp = matrix[i][j]                     #Antes, los elementos principales de la matriz se reducen todos a 1, entonces el divisor para hacerla cero aquí es él mismo (x / 1 = x)
            for k in range(j, col):                 # matriz [i] [k] es el k-ésimo valor en la i-ésima fila, y el j-ésimo número en esta fila se restablece a cero. Los otros números en esta fila deben ser la misma operación
                matrix[i][k] = matrix[i][k] - matrix[j][k] * temp   #matrix [j] [k] es el valor de la columna correspondiente en la fila pivote correspondiente a la matriz [i] [k]

def judge(matrix):                      # Determinar el número de soluciones del sistema de ecuaciones lineales mediante la matriz escalonada
    row = matrix.shape[0]
    col = matrix.shape[1]
    vanumlist = []
    for i in range(0, col):             # Debido a que la función de resolución determina una matriz de escalera de filas, solo es necesario determinar el número de números distintos de cero en la última fila. Si no hay ninguna o más de una, demuestre que hay varias soluciones; si hay una, no hay solución; si hay dos, demuestre que hay soluciones únicas
        if matrix[row - 1][i] != 0:
            vanumlist.append(matrix[row - 1][i])    #Cada vez que se atraviesa un valor distinto de cero, se escribe en la lista de vanumlist y, finalmente, se puede calcular la longitud de vanumlist
    if len(vanumlist) == 1:
        print( 'El sistema de ecuaciones no tiene solución')
    elif len(vanumlist) == 2:
        to_one(matrix)                  #Si hay una solución única, entonces la matriz se transforma aún más en la matriz de filas más simple para encontrar la solución.
        print_matrix('El paso más simple de la matriz es:', matrix)
        for i in range(0, row):
            print("x%d = %4.2f" %(i,matrix[i][col - 1]), end="  ")
    else:
        print( 'Múltiples soluciones de ecuaciones')


A = np.array([[3, 2, -6, 5, -6], [3, 2, -2, 15, 5], [3, 1, -1, -2, 1], [5, -9, -6, 20, 1], [8, 1, -15, 4, 2]])
solve(A)