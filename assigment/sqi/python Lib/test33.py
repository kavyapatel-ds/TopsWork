# sorting function
# 1 np.sort()
import numpy as np
arr=np.array([30,10,50,20])
sorted_arr=np.sort(arr)
print("original array:",arr)
print("sorted array:",sorted_arr)

# 2 np.argsort()
import numpy as np
arr=np.array([30,10,50,20])
sorted_arr=np.sort(arr)
indices=np.argsort(arr)
print(sorted_arr)
print("array:",arr)
print("indices that sort the array:",indices)
print("sorted using indices:",arr[indices])