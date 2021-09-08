#extracao de elementos


#primeiro elemento x[0]
#segundo elemento x[1]
#ultimo elemento x[-1]
#penultimo elemento x[-2]


import numpy as np

x = np.linspace(start=10, stop=100, num=10)
print('x:', x)
print('shape:', x.shape)

print('primeiro elemento:', x[0])
print('segundo elemento:', x[1])
print('ultimo elemento:', x[-1])
