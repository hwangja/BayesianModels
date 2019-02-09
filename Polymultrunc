import numpy as np
from numpy.polynomial import polynomial as P

def polymultrunc(p0, p1, m):
    p_new = P.polymul(p0, p1)
    p_new = p_new[:m]
    return p_new

p0 = [1,2,3]
p1 = [3,2,1]
p_new = polymultrunc(p0, p1, 3)

print p_new 