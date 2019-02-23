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
        expected = {1, 2, 4};
        results = generate_u_constants(m, c);
        for i,j in zip(expected, results):
            self.assertEqual(i, j)

    def test_generate_u_constants_negative_terms(self):
        """ Exception management??"""    

    def test_generate_u_constants(self):
        """ """
        m = 2
        c = 5
        expected_result = {1, 14}
        print("in actual test")
        for i in generate_u_constants(m, c):
            print(i)
        print("out of actual test")
 #       self.assertEquals(expected_result, generate_u_constants(m, c))

    def test_generate_u_constants_consistency_check(self):
        """ """

if __name__ == '__main__':
    unittest.main() 

