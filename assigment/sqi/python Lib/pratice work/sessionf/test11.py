# given arr=np.array([[1,2,3],[4,5,6]]) .flatten() ravel()

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
a=arr.flatten()
b=arr.ravel()
a[0]=100
b[0]=200
print(arr)
print(a)
print(b)