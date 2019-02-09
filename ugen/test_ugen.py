import unittest
from ugen import generate_constant, poly_mult_trunc

class UGenTestCase(unittest.TestCase):
    """ Testing U Constant Generator functions """

    # Poly Mult Trunc Unit Test
    
    # Generate Constant
    def test_generate_constant_zero_base_case(self):
        # self.assertEquals(1, generate_constant(0, 0))
        self.assertFalse(generate_constant(0, 0))

    def test_generate_constant_one_base_case(self):
        m = 2
        c = 2
        summation = 0
        for j in range(2, c):
            summation += j
        self.assertFalse(generate_constant(0, 0))
        # self.assertEquals(summation, generate_constant(m, c))

    def test_generate_constant_negative_terms(self):
        """ Exception management??"""    

    def test_generate_constant(self):
        """ """
        m = 2
        c = 5
        expected_result = {1, 14}
        self.assertEquals(expected_result, generate_constant(m, c))

    def test_generate_constant_consistency_check(self):
        """ """

if __name__ == '__main__':
    unittest.main() 

