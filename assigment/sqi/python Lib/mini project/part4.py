# statistical Analysis
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
# total revenue
discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity
print("total revenue:",np.sum(revenue))
print("average revenue:",np.mean(revenue))
print("maximum revenue:",np.max(revenue))
print("mininum revenue:",np.min(revenue))
print("mean price:",np.mean(prices))
print("median prices:",np.median(prices))
print("standard deviation:",np.std(prices))
print("mean quantity:",np.mean(quantity))
