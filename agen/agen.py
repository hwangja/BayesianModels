import numpy as np
from numpy.polynomial import polynomial as P

def generate_a(H):
    '''
    input:
    H: exponential terms for the polynomial
    
    output:
    A: polynomial coefficients
    '''
    
    A = [1]
    for j, h in enumerate(H):
        for i in range(h):
            A = P.polymul(A, [j,1])
    return A

#testing    
H = [x for x in range(50)][::-1]
print(H)
A = generate_a(H)
print(A)
print(len(A))
