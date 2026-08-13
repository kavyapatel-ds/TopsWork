# slicing
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity

# frist20
print(prices[:20])

# last20
print(prices[-20:])
# 100 to 150
print(prices[100:151])
# 5 mo product
print(prices[::5])