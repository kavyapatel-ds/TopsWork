# given [[1,2],[3,4] append columm[7,8]

import numpy as np
arr=np.array([[1,2],[3,4]])
print(np.append(arr,[[7],[8]],axis=1))