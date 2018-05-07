#!/usr/bin/env python3

import sys
import pandas as pd

cats = {}
with open('cats.txt', 'r') as f:
    for line in f:
        s = line.split()
        cats[int(s[0])] = s[1]

myid = int(sys.argv[1]) - 1

fname = 'iris_split_%s.hdf' % cats[myid]
d = pd.read_hdf(fname, 'iris', format='table')

fout = 'iris_split_%s_desc.hdf' % cats[myid]
d['SepalLength'].describe().to_hdf(fout, 'iris', format='table')
