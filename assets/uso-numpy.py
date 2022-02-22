""" 
 Resolver con numpy
 
    3a + 2b - 6c  + 5d  - 6e = 2 
    3a + 2b - 2c  + 15d + 5e = 5
    3a + b  - c   - 2d  + e  = 7
    5a - 9b - 6c  + 20d + e  = 10
    8a + b  - 15c + 4d  + 2e = 0

"""
import numpy as np
import numpy.linalg as lin


A = np.array([[3, 2, -6, 5, -6], [3, 2, -2, 15, 5], [3, 1, -1, -2, 1], [5, -9, -6, 20, 1], [8, 1, -15, 4, 2]])

B = np.array([[2],[5],[7],[10],[0]])
x = lin.solve(A,B)

for i in range(0, len(x)):
	print("x_"+str(i+1)+" = "+str(x[i]))
