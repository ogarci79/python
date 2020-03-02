#!/usr/bin/env python

import numpy as np
import pandas as pd

 #datai = pd.DataFrame.from_csv('words.csv', index_col=['Month', 'Factory'])
data = pd.read_csv('words.csv')

words = data['Word']

w = open('wordss.txt','w')

for i in data['Word']:
    w.write('% ' % i )

w.close()
