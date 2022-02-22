



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
                division=matriz[i][j]/matriz[j][j]
                
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
            print(suma)
        #Insertar las respuestas en x
        
        x[i-1]=((matriz[i-1][n]-suma)/matriz[i-1][i-1])	
        print("i={0} x={1} suma={2}".format(i, x, suma))

########################### PRUEBAS ###############################

matriz = [[3,2,3,3,10], [3,2,1,-6,2], [5,1,3,12,6], [-4,-4,8,1,5]]
n = len(matriz)

dividir_por_diagonal(matriz, n)

x = generar_x(n)

obtener_vector_resultados(matriz, n, x)
print(x)
