# identify high revenue products
import numpy as np
revenue=np.array([1000,1000,1200,900,1400,1500])
high_revenue_products=np.where(revenue>1000)
print("indices with revenue>1000:",high_revenue_products)
print("revenue values:",revenue[high_revenue_products])