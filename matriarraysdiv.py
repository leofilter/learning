#divisao

import numpy as np

x = np.ones((2,2))
y = np.eye(2)
print ('divisao de dois arrays:\n', x / y)
print ('divisao com float/int:\n', x / 2)   #broadcasting
