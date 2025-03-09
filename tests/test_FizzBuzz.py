from coe_6710110239.FizzBuzz import FizzBuzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_up_to_1(self):
        self.assertEqual(FizzBuzz(1), ["1"])

    def test_fizzbuzz_up_to_3(self):
        self.assertEqual(FizzBuzz(3), ["1", "2", "Fizz"])
    
    def test_fizzbuzz_up_to_5(self):
        self.assertEqual(FizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
    
    def test_fizzbuzz_up_to_15(self):
        self.assertEqual(FizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
    
    def test_fizzbuzz_up_to_0(self):
        self.assertEqual(FizzBuzz(0), [])
    
    def test_fizzbuzz_negative_number(self):
        self.assertEqual(FizzBuzz(-5), [])
    
    def test_fizzbuzz_large_number(self):
        self.assertEqual(FizzBuzz(20)[-1], "Buzz")  
    
    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            FizzBuzz("ten")
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            FizzBuzz(None)