import numpy as np
prices=np.array([100,200,150,300,250])
print("missing values in prices:",np.isnan(prices))
# calculate average price ignoring nan
avg_price=np.nanmean(prices)
print("average price:",avg_price)
# replace nan with average price
prices=np.where(np.isnan(prices),avg_price,prices)
print("cleaned pricrs:",prices)