# create array from 1 to 12 split into 3 equal parts 
# split into 3 equal parts 
#delete last element from each parts
# combine remaining element

import numpy as np
arr=np.arange(1,13)
parts=np.split(arr,3)
p1=np.delete(parts[0],3)
p2=np.delete(parts[1],3)
p3=np.delete(parts[2],3)
result=np.concatenate((p1,p2,p3))
print(result)