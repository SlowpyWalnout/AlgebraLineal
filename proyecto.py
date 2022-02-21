


# pasar en una función las líneas 16-24

# donde matriz es una lista de dos dimensiones con las filas de la matriz
# y n = len(matriz)
def recorrer_matriz_1(matriz, n):
    # recorremos las columnas, porque estamos incluyendo los resultados
    for j in range(0,n+1):
        # recorremos las filas
        for i in range(0, n):
            # Dejamos intacta la fila superior
            if i>j:
                # Dividir la posición de la matriz por la diagonal anterior
                division=matriz[i][j]/matriz[j][j]
                
                # Recorremos de las columnas de la fila actual
                for k in range(0, n+1):
                    # Restamos a cada posición de la fila
                    matriz[i][k]=matriz[i][k]-division*matriz[j][k];
                
                #matriz[1][1]=matriz[1][1]-(matriz[1][0]/matriz[0][0])*matriz[0][1]
                # cuando i = 1, j= 0, k = 0

def generar_x(n):
    x = []
    for _ in range(0, n):
        x.append(0)
    return x

# pasar en una función las líneas 27-32
def recorrer_matriz_2(matriz, n, x):
    # Recorremos las columnas en orden inverso
    for i in range(n,0,-1):
        suma=0
        print("posicion de i", i, " x", x, " suma", suma)
        
    #Recorre las 
        for j in range(i,n):
            print("matriz[i-1][j]",matriz[i-1][j])
            suma=suma+matriz[i-1][j]*x[j]
        #Obtener los valores de las variables
        x[i-1]=((matriz[i-1][n]-suma)/matriz[i-1][i-1])	

########################### PRUEBAS ###############################

matriz = [[3,2,3,3], [1,3,1,-6], [5,1,3,12]]
n = len(matriz)

recorrer_matriz_1(matriz, n)

x = generar_x(n)

recorrer_matriz_2(matriz, n, x)

