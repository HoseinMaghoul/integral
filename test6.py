import random
import math


total_numebr = 1_000_000
count = 0

xpoints = [random.uniform(0, 5) for _ in range(total_numebr)]
ypoints = [random.uniform(0, 1) for _ in range(total_numebr)]


for x, y in zip(xpoints, ypoints):
    if y <= math.exp(-(x**2)):
        count += 1



print(f"the integral is {5 * (count/total_numebr):.3f}")