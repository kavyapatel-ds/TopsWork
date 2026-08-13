# 3.NP.WHERE()
import numpy as np
arr=np.array([5,10,15,20,25])
indices=np.where(arr>15)
print("array:",arr)
print("indices where values>15:",indices)
print("values greater than 15",arr[indices])