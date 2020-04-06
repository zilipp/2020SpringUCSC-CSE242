import numpy as np
from numpy.random import shuffle, randint, seed

arr = [1,1,1,1,1,1,2,2,2,3]
shuffle(arr)


a, b, c = 0, 0, 0
for i in range(100):

    indeces = np.random.choice(arr, 3)
    for j in range(len(indeces)):
        if indeces[j] == 1:
            a += 1
        elif indeces[j] == 2:
            b += 1
        else:
            c += 1
print(a, b, c)
