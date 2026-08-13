# generate  a 3*3 random integer matrix between 1 and 20 fint its standard deviation and variace

import numpy as np
arr=np.random.randint([1,21,3,3])
print(arr)
print("standard diviation:",np.std(arr))
print("variance:",np.var(arr))