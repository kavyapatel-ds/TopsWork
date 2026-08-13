# combined conditions

import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity

#Find products where Price > ₹1000 AND Rating > 4
print(np.where((prices>1000)&(ratings>4)))

#Find Discount > 25% AND Quantity > 50
print(np.where((discount>25)&(quantity>50)))

#Price < ₹300 OR Rating < 2
print(np.where((prices<300)|(ratings<2)))

