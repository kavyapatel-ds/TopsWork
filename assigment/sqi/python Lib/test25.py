# indexing with np.where
import numpy as np
arr=np.array([15,10,15,20])
indices=np.where(arr>11)
print("indicies:",indices)
print("values:",arr[indices])