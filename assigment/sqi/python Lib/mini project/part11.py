# revenue categories
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity

# Low Revenue (< ₹20,000)
low=np.sum(revenue<20000)
print(low)

# medium 
medium=np.sum((revenue>2000)&(revenue<8000))
print(medium)


# high
high=np.sum(revenue>8000)
print(high)