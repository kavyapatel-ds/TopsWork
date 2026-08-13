# identify best selling product
import numpy as np
revenue=np.array([1000,1000,1200,900,1400,1500])
best_product_index=np.argmax(revenue)
print("Best selling product index:",best_product_index)
print("revenue generated:",revenue[best_product_index])
