import numpy as np
from numpy.polynomial import polynomial as P

def polynomial_truncated_multiplication(polynomial_0, polynomial_1, term_count):
    '''
    multiply two polynomails and truncated the output to desired size
    
    inputs
    polynomial_0: the original polynomial, stored as numpy array
    polynomial_1: the polynomia to be mergedl, stored as numpy array
    term_count: number of output polynomial terms excluding the constant
    
    returns
    updated polynomial
    
'''
    updated_polynomial = P.polymul(polynomial_0, polynomial_1)
    updated_polynomial = updated_polynomial[:term_count + 1]
    return updated_polynomial

def makeJ(j, m):
    '''
    make an array of 1, j, j^2,..., j^m
    
    inputs
    j: int
       product iterator
    m: int
       number of terms kept
    
    Returns
    J: array
       [1, j, j^2,..., j^m]
    '''
    return np.power(j,range(m+1))

def generate_u_constants(c, m):
    '''
    make Uis from paper
    
    inputs
    c: int
       number of terms multiplied
    m: int
       number of terms kept
       
    Returns
    U: array
       Array containing U's from paper
    '''
    U = makeJ(2, m)
    for i in range(c+1)[3:]:
        U = U
        U = polynomial_truncated_multiplication(U, makeJ(i, m), m)
    return U

if __name__ == "__main__":
        
    U = generate_u_constants(3, 3)
    print(U)
