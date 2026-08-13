# random array generation

import numpy as np
np.random.seed(30)
print("unform:",np.random.rand(2,2))
print("normal:",np.random.randn(2,2))
print("random integers:",np.random.randint(1,10,(2,3)))
print("random choice:",np.random.choice([10,20,30],size=9))