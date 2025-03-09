import unittest
from coe_6710110239.funnyString import funny_string

class TestFunnyString(unittest.TestCase):  
    def test_funny_string_dfhj(self):
        self.assertEqual(funny_string("dfhj"), "Funny")  

    def test_funny_string_abcd(self):
        self.assertEqual(funny_string("abcd"), "Funny")  

    def test_two_characters_funny_zx(self):
        self.assertEqual(funny_string("zx"), "Funny")  
    
    def test_two_characters_funny_az(self):
        self.assertEqual(funny_string("az"), "Funny")  

    def test_palindrome_funny(self):
        self.assertEqual(funny_string("racecar"), "Funny")

    def test_random_not_funny(self):
        self.assertEqual(funny_string("hello"), "Not Funny")
    
    def test_all_same_character(self):
        self.assertEqual(funny_string("kkkkk"), "Funny")

    def test_long_funny_string(self):
        self.assertEqual(funny_string("zxvtrpnmkjihgfedcba"), "Not Funny")

    def test_long_not_funny_string(self):
        self.assertEqual(funny_string("qwertyuiopasdfghjklzxcvbnm"), "Not Funny")

    def test_alternating_characters(self):
        self.assertEqual(funny_string("abababab"), "Funny")
