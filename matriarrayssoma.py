#soma

import numpy as np

x = np.ones((2,2))
y = np.eye(2)
print ('soma de dois arrays:\n', x + y)
print ('soma com float/int:\n', x + 2)   #broadcasting
