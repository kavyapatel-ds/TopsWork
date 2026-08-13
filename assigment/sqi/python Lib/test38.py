# np.clip()
import numpy as np
arr=np.array([2,5,10,9,11,15,20])
clipped=np.clip(arr,8,12)
print("original array:",arr)
print("clipped array:",clipped)