# create two matrices : a(2*3) and b(3*2) transpose a and verify is shape

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("original shape:",a.shape)
AT=a.T
print("transpose:")
print(AT)
print("transpose shape:",AT.shape)


           
           
           