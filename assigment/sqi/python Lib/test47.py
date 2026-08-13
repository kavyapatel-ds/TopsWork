import numpy as np
prices=np.array([100,200,150,300,200,250])
quantity=np.array([10,5,8,3,7,6])
revenue=np.array([1000,1000,1200,900,1400,1500])
print("number of product:",prices.size)
print("total revenue:",np.sum(revenue))
print("average price:",np.mean(prices))
print("average quantity sold:",np.mean(quantity))