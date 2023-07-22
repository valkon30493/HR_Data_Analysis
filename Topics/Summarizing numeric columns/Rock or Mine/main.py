import pandas as pd
df = pd.read_csv('data\dataset\input.txt')
rocks = df.loc[df.labels == 'R', 'null_deg']
mines = df.loc[df.labels == 'M', 'null_deg']
print('M = {} R = {}'.format(round(mines.median(), 3), round(rocks.median(), 3)))

