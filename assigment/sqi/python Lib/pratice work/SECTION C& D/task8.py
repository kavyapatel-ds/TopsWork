# create array =[-3,-1,0,1,3]apply .squre .squre root

import numpy as np
arr=np.array([-3,-1,0,1,3])
print("square:",np.square(arr))
print("square Root:",np.sqrt(arr[arr>=0]))