import pandas as pd 
import numpy as np
import os

def format_all_csv(n, m):
    parent_dir = os.getcwd()
    outputDir = 'output_trend'
    path = os.path.join(parent_dir, outputDir)
    os.chdir(path)

    total_profit_g = []
    time_spent_g = []
    total_profit_e = []
    time_spent_e = []

    profit_greedy = np.zeros((10, 10))
    profit_exact = np.zeros((10, 10))
    time_greedy = np.zeros((10, 10))
    time_exact = np.zeros((10, 10))

    for i in m:
        m_dir = os.path.join(path, str(i))
        for j in n:
            n_dir = os.path.join(m_dir, str(j))
            os.chdir(n_dir)
            df1 = pd.read_csv('greedy_result.csv', header=0)
            df2 = pd.read_csv('exact_result.csv', header=0)
            
            total_profit_g.append(df1['total'][0])
            time_spent_g.append(df1['time'][0])
            total_profit_e.append(df2['total'][0])
            time_spent_e.append(df2['time'][0])



    # os.chdir(parent_dir)
    # df.to_csv('result.csv')
