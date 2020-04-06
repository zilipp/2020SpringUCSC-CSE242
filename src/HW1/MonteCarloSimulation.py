import numpy as np
from numpy.random import shuffle, randint, seed

seed(213)   # DON'T CHANGE

### YOUR CODE HERE ###
mean_winnings = 0

num_trials = 100000
# This sets the feedback interval so we know the program hasn't crashed.
feedback = int(np.round(num_trials / 10))
earns_money = 0

# red : 1, green : 2; blue : 3
red = [1] * 60
green = [2] * 30
blue = [3] * 10
balls = red + green + blue
shuffle(balls)


for t in range(1, num_trials + 1):
    # To see the progress.
    if t % feedback == 0:
        print(np.round(100 * t / num_trials, 1), '%  complete:   earned money expectation =', earns_money / t)
    indices = np.random.choice(100, 3, replace=False)
    chosen = [balls[indices[0]], balls[indices[1]], balls[indices[2]]]
    red_num = chosen.count(1)
    toll = randint(1, 7)
    if red_num > 1:
        earns_money += toll
    else:
        earns_money -= toll
        shuffle(balls)

mean_winnings = earns_money / num_trials
print('mean winnings =', mean_winnings)