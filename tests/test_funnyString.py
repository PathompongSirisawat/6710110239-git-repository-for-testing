import unittest
from coe_6710110239.funnyString import funny_string

class TestFunnyString(unittest.TestCase):  
    def test_simple_funny(self):
        self.assertEqual(funny_string("dfhj"), "Funny")  
    
    def test_simple_funny(self):
        self.assertNotEqual(funny_string("abcd"), "Not Funny")  
    
    def test_two_characters_funny(self):
        self.assertEqual(funny_string("zx"), "Funny")  
    
    def test_two_characters_funny(self):
        self.assertEqual(funny_string("az"), "Funny")  

    def test_palindrome_funny(self):
        self.assertEqual(funny_string("racecar"), "Funny")

    def test_random_not_funny(self):
        self.assertEqual(funny_string("hello"), "Not Funny")
    
    def test_all_same_character(self):
        self.assertEqual(funny_string("kkkkk"), "Funny")

    def test_long_funny_string(self):
        self.assertNotEqual(funny_string("zxvtrpnmkjihgfedcba"), "Funny")

    def test_long_not_funny_string(self):
        self.assertEqual(funny_string("qwertyuiopasdfghjklzxcvbnm"), "Not Funny")

    def test_alternating_characters(self):
        self.assertNotEqual(funny_string("abababab"), "Not Funny")
