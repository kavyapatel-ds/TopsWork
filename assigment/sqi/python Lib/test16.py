# basic mathematical functions
import numpy as np
a=np.array([4,9,19])
b=np.array([2,3,4])
c=np.array([2,8,4])

print("add:",np.add(a,b))
z=np.add(a,b)
print(np.add(z,c))
print("subtract:",np.subtract(a,b))
print("multiply:",np.multiply(a,b))
print("divide:",np.divide(a,b))
print("power:",np.power(a,2))
print("mod:",np.mod(a,b))
print(" squre root:",np.sqrt(a))
print("exponential:",np.exp(a))
print("natural log:",np.log(a))
print("log bas 10:",np.log10(a))