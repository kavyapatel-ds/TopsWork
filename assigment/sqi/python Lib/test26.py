# session7-array manipulation
#1. np.concatenate
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.array([[9,10],[11,12]])
print("concatenate axis=0:\n",np.concatenate((a,b,c)))
print("concatenate axis=0:\n",np.concatenate((a,b,c),axis=0))
print("concatenate axis=1:\n",np.concatenate((a,b,c),axis=1))
