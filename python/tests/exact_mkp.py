from mkp.algorithms import mtm
import numpy as np
import time

n = 100
m = 10

rng = np.random

# weights
w = rng.randint(1, 51, size=n)
# profits
p = rng.randint(1, 51, size=n)
# capacities
c = []
lower_index = 0
for i in range(m):
    if i < m - 1:
        upper_index = rng.randint(w.size//(m + 1), w.size//m) + lower_index
        c.append(w[lower_index:upper_index].sum())
    else:
        c.append(w[lower_index:].sum())
    lower_index = upper_index
# c = np.array(c)

start = time.perf_counter()
w = w.tolist()
p = p.tolist()
z,x,bt,glopt = mtm(p, w, c)
print('Total profit: %d' % z)
print('Solution: %s' % x)
print('Number of backtracks performed: %d' % bt)
print('Global optimum: %s' % glopt)
print('Time spent: %.5f' % round(time.perf_counter() - start, 5))