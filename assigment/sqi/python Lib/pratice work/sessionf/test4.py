# given [1,2],[3,4] insert a new row [5,6] at index 1
import numpy as np 
arr=np.array([[1,2],[3,4]])
print(np.insert(arr,1,[5,6],axis=0))

