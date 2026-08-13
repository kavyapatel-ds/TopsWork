# print all arrays
import numpy as np
np.random.seed(42)
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
print("prices:",prices)
print("quantity:",quantity)
print("Discount:",discount)
print("ratings:",ratings) 

# 2. shape
import numpy as np
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
print(prices.shape)
print(quantity.shape)
print(discount.shape)
print(ratings.shape)

#3.size
import numpy as np
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
print(prices.size)
print(quantity.size)
print(discount.size)
print(ratings.size)

#4 datatype
import numpy as np
prices=np.random.randint(50,2001,500)
quantity=np.random.randint(1,101,500)
discount=np.random.randint(0,41,500)
ratings=np.round(np.random.uniform(1.0,5.0,500),1)
print(prices.dtype)
print(quantity.dtype)
print(discount.dtype)
print(ratings.dtype)