# create arr= np.array([1,2,3,4])
# create view_arr using view()
# create copy_arr using copy()
# modify arr[0]=arr print all three arrys explain what happend

import numpy as np
arr=np.array([1,2,3,4]) 
view_arr=arr.view()
copy_arr=arr.copy()
arr[0]=999
print("original:",arr)
print("view:",view_arr)
print("copy:",copy_arr)