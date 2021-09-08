#subtracao

import numpy as np

x = np.ones((2,2))
y = np.eye(2)
print ('subtracao de dois arrays:\n', x - y)
print ('subtracao com float/int:\n', x - 2)   #broadcasting
