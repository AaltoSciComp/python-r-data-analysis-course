#!/usr/bin/env python3

import pandas as pd
import scipy.stats as stats

# First figure out how many datasets we have by reading the previously
# created cats.txt
cats = []
with open('cats.txt') as f:
    for line in f:
        cats.append(line.split()[1])
d = {}
for c in cats:
    d[c] = pd.read_hdf('iris_split_%s_desc.hdf' % c, 'iris', format='table')

print("""Mean Sepal length per species:
NAME        SepalLength
=========================
""")

for c in cats:
    print("%9s         %7g" % (c, d[c].loc['mean']))


ds = d['Iris-setosa']
dv = d['Iris-versicolor']
print("\nIndependent t-test for Setosa and Versicolor sepal lengths:",
      stats.ttest_ind_from_stats(ds.loc['mean'], ds.loc['std'], ds.loc['count'],
                                 dv.loc['mean'], dv.loc['std'], dv.loc['count'],
                                 equal_var=False))

