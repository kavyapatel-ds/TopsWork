# create a random integer matrix of shape 3*3 with values between 10 and 30

import numpy as np
np.random.seed(42)
arr=np.random.randint(10,50,(3,3))
print(arr)
