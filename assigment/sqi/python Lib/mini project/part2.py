# DATA CLEANNING
# MISSING RATINGS COUNT
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
prices[np.random.choice(500, 15, replace=False)] = 0
ratings[np.random.choice(500, 10, replace=False)] = np.nan
print("missing ratings:",np.isnan(ratings).sum())

# replace missing ratings with average ratings
avg_ratings=np.nanmean(ratings)
ratings=np.where(np.isnan(ratings),avg_ratings,ratings)
print("average ratings:",avg_ratings)
print("rating after cleanning:",ratings)

# count products whose price is zero
print("zero price produccts:",np.sum(prices==0))

# replace zero prices with average price of valid products 
avg_price=np.mean(prices[prices !=0])
prices=np.where(prices ==0,avg_price,prices)
print("average price:",avg_price)
print("prices after cleaning:",prices)

