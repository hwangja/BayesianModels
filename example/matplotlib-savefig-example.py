"""
Your module description
"""

import pandas as pd
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt

p_dist = np.random.poisson(5,100)
print(p_dist)

fig, ax = plt.subplots(1, 1)
ax.hist(p_dist)
fig.savefig('testfig')
