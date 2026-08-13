# summary report
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)

discount_amount=(prices*discount)/100
final_prices=prices-discount_amount
revenue=final_prices*quantity

print("total products:",prices.size)
print("average prices:",np.mean(prices))
print("Total Products:",prices.size)

print("Average Price:",np.mean(prices))

print("Average Discount:",np.mean(discount))

print("Average Rating:",np.mean(ratings))

print("Average Quantity:",np.mean(quantity))

print("Total Revenue:",np.sum(revenue))

print("Highest Revenue:",np.max(revenue))

print("Lowest Revenue:",np.min(revenue))

print("High Revenue Products:",np.sum(revenue>80000))

print("Highly Rated Products:",np.sum(ratings>4.5))

print("Expensive Products:",np.sum(prices>1500)) 