# Unique Analysis
#Find Unique discount percentages
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity
#unique Discount
unique=np.unique
print(unique)

# count
print(len(unique))

#frequency
value,count=np.unique(discount,return_counts=True)
print(value)
print(count)
