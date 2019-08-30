from __future__ import division
import numpy as np
import time

def main():
    n = 100
    m = 10
    p, w, c = generate_random_data(n, m)
    
    start = time.perf_counter()
    
    y = [0]*n
    c_bar = [0]*m
    z = [0]*n

    for j in range(n):
        y[j] = -1

    for i in range(m):
        c_bar[i] = c[i]
        greedy(i, n, c_bar, y, z, p, w)
    
    print('Total profit: %d' % sum(z))
    print('Solution: %s' % y)
    print('Time spent: %.5f' % round(time.perf_counter() - start, 5))


def greedy(i, n, c_bar, y, z, p, w):
    for j in range(n):
        if y[j] == -1 and w[j] < c_bar[i]:
            y[j] = i
            c_bar[i] = c_bar[i] - w[j]
            z.append(p[j])


def generate_random_data(n, m):
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
    c = np.array(c)

    return p, w, c

if __name__ == '__main__':
    main()