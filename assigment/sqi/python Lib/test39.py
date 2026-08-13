# handling nan values
import numpy as np
arr=np.array([10,20,np.nan,40])
print("array:",arr)
print("mean:",np.nanmean(arr))
print("sum:",np.nansum(arr))
print("standard deviation:",np.nanstd(arr))