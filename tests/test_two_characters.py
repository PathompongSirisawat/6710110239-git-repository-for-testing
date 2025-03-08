from coe_6710110239.two_characters import alternate
import unittest

class TestTwoCharacters(unittest.TestCase):
    def test_basic_alternating(self):
        self.assertEqual(alternate("abaacdabd"), 4) 
    
    def test_no_valid_alternation(self):
        self.assertEqual(alternate("aaaa"), 0)
    
    def test_max_alternating_length(self):
        self.assertEqual(alternate("abacabad"), 3) 
    
    def test_single_character_string(self):
        self.assertEqual(alternate("a"), 0)
    
    def test_two_character_string(self):
        self.assertEqual(alternate("ab"), 2)
    
    def test_three_character_string(self):
        self.assertEqual(alternate("abc"), 2)
    
    def test_alternating_with_non_alpha_chars(self):
        self.assertEqual(alternate("a1b1a1b1"), 4)  
    
    def test_string_with_spaces(self):
        self.assertEqual(alternate("a b a b"), 4)
    
    def test_large_input(self):
        self.assertEqual(alternate("abababababababababababababababababababab"), 40)

    def test_input_none(self):
        with self.assertRaises(TypeError):
            alternate(None)

    def test_input_integer(self):
        with self.assertRaises(TypeError):
            alternate(12345)

