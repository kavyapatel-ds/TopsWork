#10.generate 1000 random numbers from normal distribution compute . mean .standard deviation 95th percentile

import numpy as np
arr=np.random.normal(size=1000)
print("mean:",np.mean(arr))
print("standard deviation:",np.std(arr))
print("as the percentile:",np.percentile(arr,95))
