import unittest
import numpy
from ugen import polynomial_truncated_multiplication, generate_u_constants, makeJ

class UGenTestCase(unittest.TestCase):
    """ Testing U Constant Generator functions """

    # Poly Mult Trunc Unit Test
    
    # Generate Constant
    def test_generate_u_constants_zero_base_case(self):
        constants_array = generate_u_constants(0,0)
        self.assertEquals(1, len(constants_array))
        self.assertEquals(1, constants_array[0])

    def test_generate_u_constants_one_base_case(self):
        m = 2
        c = 2
        expected = [1, 2, 4];
        results = generate_u_constants(c, m);
        for i,j in zip(expected, results):
            self.assertEqual(i, j)

    @unittest.skip("code not yet performing correctly with negative 'c'")
    def test_generate_u_constants_negative_terms(self):
       """ Exception management??"""    
 
    def test_generate_u_constants(self):
        """ """
        m = 2
        c = 3
        expected = [1, 5, 19]
        results = generate_u_constants(c, m);
        for i,j in zip(expected, results):
            self.assertEqual(i, j)
 

    def test_generate_u_constants_consistency_check(self):
        """ """
        m = 5
        c = 10
        expected = [1, 54, 1650, 37620, 713427, 11909898]
        result =  generate_u_constants(c, m)
        for i,j in zip(expected, result):
            self.assertEquals(i, j)

if __name__ == '__main__':
    unittest.main() 

