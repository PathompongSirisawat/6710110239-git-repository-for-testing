from coe_6710110239.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_5_8_is_not_prime(self):
        prime_list = [2, 5, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_1_3_5_7_9_is_not_prime(self):
        prime_list = [1, 3, 5, 7, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_107_211_503_is_prime(self):
        prime_list = [107, 211, 503]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_char_t_is_error(self):
        prime_list = ["t"]  
        with self.assertRaises(TypeError):  
            is_prime_list(prime_list)
    
    def test_give_1_3_5_char_x_is_error(self):
        prime_list = [1, 3, 5, "x"]  
        with self.assertRaises(TypeError):  
            is_prime_list(prime_list)

    def test_give_empty_list_is_not_prime(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)