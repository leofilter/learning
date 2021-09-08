#soma, subtracao e divisao

import numpy as np

x = np.ones((2,2))
y = np.eye(2)
print ('combinacao de operacoes:\n', (x + y) / (x - 2))
