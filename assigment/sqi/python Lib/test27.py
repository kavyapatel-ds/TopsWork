# 2. stackingfunctions

import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=np.array([9,10,11,12])
print("vstack:\n",np.vstack((a,b,c)))
print("hstack:\n",np.hstack((a,b,c)))
print("dstack:\n",np.dstack((a,b,c)))

a=np.array([2,4,5,7,True,"kavya"])
a=np.array([2,4,5,True,False,7])
print(a)