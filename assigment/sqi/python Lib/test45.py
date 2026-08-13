# sorting product by revenue
import numpy as np
revenue=np.array([1000,1000,1200,900,1400,1500])
sorted_indices=np.argsort(revenue)
print("sorted product indicies:",sorted_indices)
print("revenue sorted:",revenue[sorted_indices])
