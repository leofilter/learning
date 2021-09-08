'''
exemplo:
solucao de sistema de equacoes:
a + 2*b = 7
3*a - 2*b = -11
solucao analitica: (a,b) = (-1,4)
matricialmente, este problema tem a seguinte forma:
Ax = c, onde:
x = [a, b]
A = [[1, 2], [3, -2]]
c = [7, -11]
solucao numerica x = inv(A) @ c,
'''

#definicao do problema
import numpy as np

A = np.array([[1,2],[3,-2]])
c = np.array([[7], [-11]])
#print ('A: \n', A)
#print ('c: \n', c)

x = np.dot(np.linalg.inv(A),c)
#x = np.linalg.inv(A) @ c
print ('(a, b):', x.ravel())
