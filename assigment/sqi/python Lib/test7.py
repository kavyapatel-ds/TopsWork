#creating special Arrays
import numpy as np
hospital=np.array([
    [ #floor1
     ["room1", "room2"],
     ["room3","room4"]
     ],
    [ # floor2
      ["room5","room6"],
      ["room7","room8"]
     ],
    [ #floor 3
     ["room9","room10"],
     ["room11","room12"]
     ]
])
print("number of dimensions:",hospital.ndim)
print("size:",hospital.size)
print("shape:",hospital.shape)
