# using logical operations given: arr=[5,10,15,25] extract values between 10 and 20 inclusive

import numpy as np
arr=np.array([5,10,15,20,25])
result=arr[(arr>=10)&(arr<=20)]
print(result)