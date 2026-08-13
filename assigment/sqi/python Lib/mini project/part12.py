# top products
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity
# top 10 revenue
top=np.argsort(revenue)[-10:]
print(top)
print(revenue[top])

# top 10 rating
top=np.argsort(ratings)[-10:]
print(top)
print(ratings[top])

# top 10 quantity
top=np.argsort(quantity)[-10:]
print(top)
print(quantity)