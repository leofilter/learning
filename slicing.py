#slicing: extracao de subarrays:

import numpy as np

x = np.linspace(start=10, stop=100, num=10)
print('x:', x)
print('shape:', x.shape)

print('dois primeiros elementos:', x[0:2])
print('dois primeiros elementos:', x[:2])
print('dois ultimos elementos:', x[-2:])
