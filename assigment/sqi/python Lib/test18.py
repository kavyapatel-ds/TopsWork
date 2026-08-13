# statistical operations reduce array
import numpy as np
data=np.array([10,24,30,36,50])
print("mean:",np.mean(data))
print("median:",np.median(data))
print("standard deviation:",np.std(data))
print("variance:",np.var(data))
print("minimum:",np.min(data))
print("maximum:",np.max(data))
print("sum:",np.sum(data))
print("cumulative sum:",np.cumsum(data))
print("product:",np.prod(data))
print("90 th percentile:",np.percentile(data,90))