# BOLLEAN INDEXING

import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity
#Products costing more than ₹1500

expensive=np.where(prices>1500)
print(expensive)
print(len(expensive))

# Products with rating greater than 4
high_rating=np.where(ratings)
print(high_rating)
print(len(high_rating[0]))

#Products with quantity sold greater than 80
high_quantity=np.where(quantity>80)
print(high_quantity)
print(len(high_quantity[0]))

# products having discount greater than30%
high_discount=np.where(discount>30)
print(high_discount)
print(len(high_discount[0]))