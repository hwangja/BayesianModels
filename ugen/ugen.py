import numpy as np
from numpy.polynomial import polynomial as P

def polynomial_truncated_multiplication(polynomial_0, polynomial_1, term_count):
    updated_polynomial = P.polymul(polynomial_0, polynomial_1)
    updated_polynomial = updated_polynomial[:term_count]
    return updated_polynomial

def makeJ(j, m):
    return np.power(j,range(m+1))

def makeU(c, m):
    U = makeJ(2, m)
    for i in range(c+1)[3:]:
        U = U
        U = polynomial_truncated_multiplication(U, makeJ(i, m), m)
    return U

if __name__ == "__main__":
        
    U = makeU(3, 3)
    print(U)
