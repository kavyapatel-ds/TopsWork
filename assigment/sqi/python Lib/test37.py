#np.isman()
import numpy as np
arr=np.array([1,np.nan,3])
print(np.isnan(arr))

# np.isinf()
import numpy as np 
arr=np.array([1,np.inf,3])
print( np.isinf(arr))

# np.isfinite()
import numpy as np
arr=np.array([1,np.nan,np.inf,np.inf,np.inf,5])
print("array:",arr)
print("isnan:",np.isnan(arr))
print("isinf:",np.isinf(arr))
print("isfinite:",np.isfinite(arr))