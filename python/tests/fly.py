from __future__ import division
from mkp.algorithms import mtm
import numpy as np
import time
import csv
import os
import shutil

def generate_dissimilar_data(n, m, ra):
    rng = np.random
    rng.seed(30)
    
    # weights
    w = rng.randint(1, ra, size=n)
    # profits
    p = rng.randint(1, ra, size=n)
    # capacities
    c = []
    lower_index = 0
    upper_index = 0
    for i in range(m):
        if i < m - 1:
            step = rng.randint(w.size//(m + 1), w.size//m + 1)
            upper_index = step + lower_index
            c.append(w[lower_index:upper_index].sum())
        else:
            c.append(w[lower_index:].sum())
        lower_index = upper_index
    w = w.tolist()
    p = p.tolist()
    print(c)
    print(sum(c), sum(w))
    return p, w, c
    
def generate_similar_data(n, m, ra):
    rng = np.random
    rng.seed(30)
    
    # weights
    w = rng.randint(1, ra, size=n)
    # profits
    p = rng.randint(1, ra, size=n)
    # capacities
    c = []
    w = w.tolist()
    p = p.tolist()
    low = 0.8*sum(w)//m
    high = 1.2*sum(w)//m
    for i in range(m):
        c.append(rng.randint(low, high)) 
    print(c)
    print(sum(c), sum(w))
    return p, w, c
    
def generate_increasing_data(n, m, ra):
    rng = np.random
    rng.seed(30)
    
    # weights
    w = rng.randint(1, ra, size=n)
    # profits
    p = rng.randint(1, ra, size=n)
    # capacities
    c = []
    lower_index = 0
    upper_index = 1
    step = 3
    for i in range(m):
        if i < m - 1:
            c.append(w[lower_index:upper_index].sum())
            lower_index = upper_index
            upper_index = upper_index + step
            step = step + 2
        else:
            c.append(w[lower_index:].sum())
    
    print(c)
    print(sum(c), sum(w))
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
    n = [10, 20, 30, 40, 50]
    m = [2, 3, 4, 5]
    
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, 'output_dissimilar')
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
            p, w, c = generate_dissimilar_data(j, i, j)
                
            start = time.perf_counter()
            z, x = heuristic(p, w, c)
            t = round(time.perf_counter() - start, 5)
            write_csv('greedy', z, t)

            start = time.perf_counter()
            z, x, _, _ = mtm(p, w, c)
            t = round(time.perf_counter() - start, 5)
            write_csv('exact', z, t)

    
    path = os.path.join(parent_dir, 'output_similar')
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
            p, w, c = generate_dissimilar_data(j, i, j)
                
            start = time.perf_counter()
            z, x = heuristic(p, w, c)
            t = round(time.perf_counter() - start, 5)
            write_csv('greedy', z, t)

            start = time.perf_counter()
            z, x, _, _ = mtm(p, w, c)
            t = round(time.perf_counter() - start, 5)
            write_csv('exact', z, t)

    path = os.path.join(parent_dir, 'output_increasing')
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
            p, w, c = generate_dissimilar_data(j, i, j)
                
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