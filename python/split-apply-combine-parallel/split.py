#!/usr/bin/env python3

import pandas as pd

import os.path
d = pd.read_csv(os.path.join(pd.__path__[0], 'tests/data/iris.csv'), dtype={'Name': 'category'})

cats = []
for g_name, g_df in d.groupby('Name'):
    g_df.to_hdf('iris_split_%s.hdf' % g_name, 'iris', format='table')
    cats.append(str(g_name))

with open('cats.txt', 'w') as f:
    for ii, nn in enumerate(cats):
        f.write('%d %s\n' %(ii, nn))
