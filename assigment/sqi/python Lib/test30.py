# copy vs view
import numpy as np
arr=np.array([1,2,3])
view_arr=arr.view()
copy_arr=arr.copy()
view_arr[0]=100
print("original:",arr)
print("view:",view_arr)
print("copy:",copy_arr)