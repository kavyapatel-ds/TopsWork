# create array from 1 to 6 reshape int 2*3matrix change element (0,1)to 100
import numpy as np
arr=np.arange(1,7)
arr=arr.reshape(2,3)
arr[0,1]=100
print(arr)