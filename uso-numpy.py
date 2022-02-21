""" 
 Resolver con numpy
 
    3a + 2b - 6c  + 5d  - 6e = 2 
    3a + 2b - 2c  + 15d + 5e = 5
    3a + b  - c   - 2d  + e  = 7
    5a - 9b - 6c  + 20d + e  = 10
    8a + b  - 15c + 4d  + 2e = 0

"""
"""
Si el primer valor es 0 de la primera ecuación se intercambia con la segunda ecuación asi hasta que el primer valor sea diferente de 0

$$$$$$$$$$

Se divide la ecuacion 1 entre el valor de la primera posición de dicha ecuación
Se multiplica la ecuacion 1 por los valores de la primera posición de las demas ecuaciones
Se resta el valor de la ecuación 1 multiplicada por cada ecuación a las demás ecuaciones respectivamente. 
Se divide la ecuación 2 entre el valor de la segunda posición de dicha ecuación.
Se repite hasta llegar al último valor de la última ecuación.
se imprimen resultados.

"""

import numpy as np
import numpy.linalg as lin

# A*x = B
## Se utilizará 
A = np.array([[3, 2, -6, 5, -6], [3, 2, -2, 15, 5], [3, 1, -1, -2, 1], [5, -9, -6, 20, 1], [8, 1, -15, 4, 2]])
AZ = [[3, 2, -6, 5, -6], [3, 2, -2, 15, 5], [3, 1, -1, -2, 1], [5, -9, -6, 20, 1], [8, 1, -15, 4, 2]]

#AN=A[N]/A[N][N]

A1=A[0]/A[0][0]
A2=A[1]/A[1][1]
A3=A[2]/A[2][2]
A4=A[3]/A[3][3]


A2_1=A2-(A1*A2[0])
A3_1=A3-(A1*A3[0])
A4_1=A4-(A1*A4[0])
print('A2_1={0}, \nA3_1={1}, \nA4_1={2}'.format(A2_1, A3_1, A4_1))

#print(A1, A2, A3, A4, A5)
print('a1={0},\na2={1},\na2={2},\na3={3}'.format(A1, A2, A3, A4))


####################################################################################

#B = np.array([[2],[5],[7],[10],[0]])
#x = lin.solve(A,B)
#print ('la solución para cada una es: ')
#print ('a', x[0])
#print ('b', x[1])
#print ('c', x[2])
#print ('d', x[3])
#print ('e', x[4])

#######################################################################################
"""
my_list = [4, 6, 8, 10]
divisor = 2

my_list = list(map(lambda x: x / divisor, my_list))
print(my_list) # [2.0, 3.0, 4.0, 5.0]
"""
