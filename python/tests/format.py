import pandas as pd 
import numpy as np
import os

def format_all_csv(n, m):
    parent_dir = os.getcwd()
    outputDir = 'output_trend'
    path = os.path.join(parent_dir, outputDir)
    os.chdir(path)

    profit_greedy = np.zeros((10, 10))
    profit_exact = np.zeros((10, 10))
    time_greedy = np.zeros((10, 10))
    time_exact = np.zeros((10, 10))

    for i in m:
        m_dir = os.path.join(path, str(i+1))
        for j in n:
            n_dir = os.path.join(m_dir, str((j+1)*10))
            os.chdir(n_dir)
            df1 = pd.read_csv('greedy_result.csv', header=0)
            df2 = pd.read_csv('exact_result.csv', header=0)
            
            profit_greedy[i, j] = df1['total'][0]
            time_greedy[i, j] = df1['time'][0]
            profit_exact[i, j] = df2['total'][0]
            time_exact[i, j] = df2['time'][0]
        
    df_pg = pd.DataFrame(data=profit_greedy[0:, 0:],
                         index=list(range(1, 10)),
                         columns=list(range(10, 110, 10)))
    
    df_tg = pd.DataFrame(data=time_greedy[0:, 0:],
                         index=list(range(1, 10)),
                         columns=list(range(10, 110, 10)))

    df_pe = pd.DataFrame(data=profit_exact[0:, 0:],
                         index=list(range(1, 10)),
                         columns=list(range(10, 110, 10)))

    df_te = pd.DataFrame(data=time_exact[0:, 0:],
                         index=list(range(1, 10)),
                         columns=list(range(10, 110, 10)))

    df_pg.to_csv('profit_greedy.csv')
    df_tg.to_csv('time_greed.csv')
    df_pe.to_csv('profit_exact.csv')
    df_te.to_csv('time_exact.csv')

if __name__ == '__main__':
    format_all_csv(10, 9)
