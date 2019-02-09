import numpy as np
from numpy.polynomial import polynomial as P

def polynomial_truncated_multiplication(polynomial_0, polynomial_1, term_count):
    updated_polynomial = P.polymul(polynomial_0, polynomial_1)
    updated_polynomial = updated_polynomial[:term_count]
    return updated_polynomial

polynomial_0 = [1,2,3]
polynomial_1 = [3,2,1]
updated_polynomial = polynomial_truncated_multiplication(polynomial_0, polynomial_1, 3)

print updated_polynomial 
