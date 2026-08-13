# create an array of numbers from 1 to 9 and
# flatten it using level()
# flatten it using flatten()
# explain the diifference

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print("original:")
print(arr)
print("ravel:")
print(arr.ravel())
print("flatten:")
print(arr.flatten())