# create an array from 1 to 9 and reshape 3*3 compute cumulative sum(cumsum)

import numpy as np
arr=np.arange(1,10).reshape(3,3)
print(arr)
print(np.cumsum(arr))