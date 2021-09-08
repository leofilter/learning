#multiplicacao matricial

import numpy as np

x = np.ones((2,2))
y = np.eye(2)
print ('multiplicacao matricial (np.dot):\n', np.dot(x,y))
print ('multiplicacao matricial (@):\n', x @ y)
print ('multiplicacao matricial (.dot):\n', x.dot(y))
