# searching
# Product having highest revenue

import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

# Product having highest revenue
discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity
index=np.argmax(revenue)
print(index)
print(revenue[index])

#Product having lowest revenue
index=np.argmin(revenue)
print(index)
print(revenue[index])

#Product having highest quantity sold
index=np.argmax(quantity)
print(index)
print(quantity[index])

#Product having highest rating
index=np.argmax(ratings)
print(index)
print(ratings[index])