#Eliminación Gaussiana
#Función para mostrar la matriz




def switch_row(i, arr):
    n = len(arr)
    if  n == i:
        return ([], 0)
    
    i_t = arr[i]
    t = arr[i+1]
    arr[i] = t
    arr[i+1] = i_t


    return (arr, 1)

def inverted_loop_rows(n,x, matriz):
    ## ciclo invertido desde n hasta 0
    for i in range(n,0,-1):
        suma=0

        ## ciclo normal desde i hasta n
        for j in range(i,n):
            suma=suma+matriz[i-1][j]*x[j]
            print(matriz[i-1][j], x[j], suma)
        
   
			
matriz = [[3, 2, -6, 5, -6, 2], [3, 2, -2, 15, 5, 5], [3, 1, -1, -2, 1, 7], [5, -9, -6, 20, 1, 10], [8, 1, -15, 4, 2, 0]]
#Orden de la matriz
n=len(matriz) 
 
#Recorrer la matriz 
for j in range(0,n+1):
	for i in range(0, n):
		if i>j:
			#Divir los elementos de la matriz
			division=matriz[i][j]/matriz[j][j]
			for k in range(0, n+1):
				#Obterner el nuevo valor para los elementos en la diagonal inferior
				matriz[i][k]=matriz[i][k]-division*matriz[j][k]
#Recorrer la matriz
x = [0,0,0,0,0]
"""
for i in range(n,0,-1):
	suma=0
	for j in range(i,n):
		suma=suma+matriz[i-1][j]*x[j]
    #Obtener los valores de las variables
        if matriz[i-1][i-1] == 0: 
            a, _ = switch_row(i, [])
    
        x[i-1]=((matriz[i-1][n]-suma)/matriz[i-1][i-1])


#Mostrar los valores de las variables
for i in range(0,n):
	print("x"+str(i)+" = "+str(x[i]))

"""
inverted_loop_rows(n, x, matriz)