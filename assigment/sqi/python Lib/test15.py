# array operations
#1. arithmetic operations

import numpy as np
a=np.array([10,20,30])
b=np.array([2,4,5])
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("power:",a**2)
print("modulus:",a%b)


# 2.comparison operators
import numpy as np
a=np.array([5,10,15])
print("greater than 8:",a>8)
print("greater than 8:",a[a>8])
print("equal to 10:",a==10)

# 3.logical operations
import numpy as np
a=np.array([5,8,15,20])
cond1=a>8
cond2=a<8
print("logical and:",np.logical_and(cond1,cond2))
print("filtere result:",a[np.logical_and (cond1,cond2)])

print("logical or:",np.logical_or(cond1,cond2))
print("logical or:",a[np.logical_or (cond1,cond2)])

print("logical NOT:", np.logical_not(cond1))
print("logical NOT:", a [np.logical_not (cond1)])


# 4. broadcasting

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
print("broadecasted addition:\n",a+b)

#5.element-wise and aggregate

import numpy as np
arr=np.array([1,2,3,4])
print(arr**2)
print(np.sum(arr))