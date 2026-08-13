import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
discount_amont=prices*discount/100
print("discount amount:",discount_amont)

# caculate final selling price
final_prices=prices-discount_amont
# calcuate revenue
revenue=final_prices*quantity
print("discount amount:",discount_amont)
print("final selling price:",final_prices)
print("revenue:",revenue)
