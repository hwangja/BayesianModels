import numpy as np
from Polymultrunc import polymultrunc

def makeJ(j, m):
    return np.power(j,range(m+1))

def makeU(c, m):
    U = makeJ(2, m)
    for i in range(c+1)[3:]:
        U = U
        U = polymultrunc(U, makeJ(i, m), m)
    return U

if __name__ == "__main__":
        
    U = makeU(3, 3)
    print(U)