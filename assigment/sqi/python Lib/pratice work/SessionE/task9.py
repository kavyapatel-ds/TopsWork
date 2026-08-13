 # 9. given array :arr =[3,6,9,12,15] use np,where () find indicies where values are greater than 18
 
import numpy as np
arr=np.array([3,6,9,12,15])
indices=np.where(arr>8)
print("indices:",indices)
print("values:",arr[indices])