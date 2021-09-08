#cria;'ao de valores dentro de um intervalo
#valroes uniformes entre 5 e 15
import numpy as np

x_min, x_max = 5, 15
x = np.linspace(start = x_min, stop = x_max, num = 6)
print('x:', x)
print('shape:', x.shape)
