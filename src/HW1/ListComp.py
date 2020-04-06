from numpy.random import randint, seed
from numpy import mean, std

# Set the seed so the same random numbers will be generated.
seed(42)

# Create a list of 22 simulated die casts (i.e., 22 random numbers from 1 to 6).
number_list = [randint(1, 7) for _ in range(22)]
print(number_list)

# Now create a list of the cubes of those of the above integers that are less than 5.
cubed = [n**3 for n in number_list if n < 5]
print(cubed)


# (a)
indices = [i for i in range(len(number_list)) if number_list[i] == 2]
print(indices)

# (b)
seed(117)
first = [randint(1, 7) for _ in range(22)]
second = [randint(1, 7) for _ in range(22)]
sums = [first[i] + second[i] for i in range(len(first))]
print(first)
print(second)
print(sums)

# (c)
seed(111)
first_100000 = [randint(1, 7) for _ in range(100000)]
second_100000 = [randint(1, 7) for _ in range(100000)]
sums = [first_100000[i] + second_100000[i] for i in range(len(first_100000))] # Replace this line

print('mean =', mean(sums), '    std =', std(sums))