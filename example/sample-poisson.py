import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
# import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.1)
d = []

for i in t:
    p = pow(5,i)
    q = p/math.factorial(i)
    d.append(q)

plt.plot( t, np.exp(5)*d, 'bs')
plt.show()
