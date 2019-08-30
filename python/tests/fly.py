from __future__ import division
from mkp.algorithms import mtm
import numpy as np
import time
import csv
import os
import shutil

# p = [110, 150, 70, 80, 30, 5]
# w = [40, 60, 30, 40, 20, 5]
# c = [65, 85]
 

def generate_random_data(n, m, ra):
    rng = np.random

    # weights
    w = rng.randint(1, ra, size=n)
    # profits
    p = rng.randint(1, ra, size=n)
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
    w = w.tolist()
    p = p.tolist()

    return p, w, c


def heuristic(p, w, c):
    n = len(w)
    m = len(c)

    y = [0]*n
    c_bar = [0]*m
    z = [0]*n

    for j in range(n):
        y[j] = -1

    for i in range(m):
        c_bar[i] = c[i]
        for j in range(n):
            if y[j] == -1 and w[j] < c_bar[i]:
                y[j] = i
                c_bar[i] = c_bar[i] - w[j]
                z.append(p[j])
    
    return sum(z), y


def write_csv(f, z, t):
    filename = '{}_result.csv'.format(f)
    with open(filename, mode='w') as csv_file:
        fieldnames = ['total', 'time']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'total': z, 'time': t})


def main():
    # n = [1000, 2000, 3000, 4000, 5000]
    # m = [20, 40, 60, 80, 100]

    n = [100, 200]
    m = [10, 20]
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, 'output')
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

    os.mkdir(path)

    for i in m:
        m_dir = os.path.join(path, str(i))
        os.mkdir(m_dir)
        for j in n:
            n_dir = os.path.join(m_dir, str(j))
            os.mkdir(n_dir)
            os.chdir(n_dir)
            p, w, c = generate_random_data(j, i, j)
            for r in range(10):
                r_dir = os.path.join(n_dir, str(r))
                os.mkdir(r_dir)
                os.chdir(r_dir)
                
                start = time.perf_counter()
                z, x = heuristic(p, w, c)
                t = round(time.perf_counter() - start, 5)
                write_csv('greedy', z, t)

                start = time.perf_counter()
                z, x, _, _ = mtm(p, w, c)
                t = round(time.perf_counter() - start, 5)
                write_csv('exact', z, t)



if __name__ == '__main__':
    main()