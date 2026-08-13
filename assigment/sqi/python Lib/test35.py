# np.nozero()
import numpy as np
arr=np.array([0,1,0,2,3,0])
print("array:",arr)
non_zero_indices=np.nonzero(arr)
print("indices of non element:",non_zero_indices)
print("non-zero values:",arr[non_zero_indices])