# creating arrays in numpy
#1.np.array
import numpy as np
arr=np.array([1,2,3,4],dtype=float)
print(arr)
print(arr.dtype)

# np.arange
import numpy as np
arr=np.arange(0,10,2)
print(arr)

# np linspace
import numpy as  np
arr=np.linspace(1,20,5)
print(arr)

#np.logspace
import numpy as np
arr=np.logspace(1,3,4)
print(arr)

# np.zeros
import numpy as np
arr=np.zeros((2,3))
print(arr)

# np.ones
import numpy as np
arr=np.ones((3,2))
print(arr)

#np.empty
import numpy as np
arr=np.empty((3,3))
print(arr)

#np.eye() and np.identity()

import numpy as np
print(np.eye(3,4))
print(np.identity(4))
a=np.identity(10)
print(a)
b=3.14*a
print(b)