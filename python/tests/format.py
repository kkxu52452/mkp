import pandas as pd 
import os

def format_all_csv(n, m):
    parent_dir = os.getcwd()
    outputDir = 'output'
    path = os.path.join(parent_dir, outputDir)
    os.chdir(path)

    total_profit_g = []
    time_spent_g = []
    total_profit_e = []
    time_spent_e = []

    for i in m:
        m_dir = os.path.join(path, str(i))
        for j in n:
            n_dir = os.path.join(m_dir, str(j))
            os.chdir(n_dir)
            for r in range(100):
                r_dir = os.path.join(n_dir, str(r))
                os.chdir(r_dir)
                df1 = pd.read_csv('greedy_result.csv', header=0)
                df2 = pd.read_csv('exact_result.csv', header=0)
                
                total_profit_g.append(df1['total'][0])
                time_spent_g.append(df1['time'][0])
                total_profit_e.append(df2['total'][0])
                time_spent_e.append(df2['time'][0])


    df = pd.DataFrame({'x': concurrency, 'y1': durations, 'y2': avg_rtts, 'y3': rqs, 'y4': failures})

    concurrency = []
    durations = []
    avg_rtts = []
    rqs = []
    failures = []

    for i in range(frm, to+step, step):
        mid = df[df['x'] == i]
        concurrency.append(i)
        durations.append(mid['y1'].mean())
        avg_rtts.append(mid['y2'].mean())
        rqs.append(mid['y3'].mean())
        failures.append(mid['y4'].mean())

    df = pd.DataFrame({'x': concurrency, 'y1': durations, 'y2': avg_rtts, 'y3': rqs, 'y4': failures})

    os.chdir(parent_dir)
    df.to_csv('result.csv')
