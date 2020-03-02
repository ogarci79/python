#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from sympy import init_session
from scipy.stats import norm

iq_mean = 100
iq_std_dev = 15
iq_distribution = norm(loc=iq_mean,scale=iq_std_dev)
for n in np.arange(8):
    print('{:6.2f}'.format(iq_distribution.rvs()))

n,bins,patches = plt.hist(data_set,59, normed=1, facecolor='g')
