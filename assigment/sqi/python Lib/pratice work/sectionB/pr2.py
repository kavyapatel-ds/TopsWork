# create a 4*4 matrix using np.arange() and transpose it.
import numpy as np
arr=np.arange(1,17).reshape(4,4)
print("original:")
print(arr)
print("transpose:")
print(arr.T)