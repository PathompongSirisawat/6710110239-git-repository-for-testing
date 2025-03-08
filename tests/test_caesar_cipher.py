from coe_6710110239.caesar_cipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_shift_lowercase(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
    
    def test_shift_uppercase(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")
    
    def test_shift_mixed_case(self):
        self.assertEqual(caesarCipher("AbC", 3), "DeF")
    
    def test_shift_with_wraparound(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")
    
    def test_shift_large_k(self):
        self.assertEqual(caesarCipher("abc", 29), "def")
    
    def test_no_shift(self):
        self.assertEqual(caesarCipher("hello", 0), "hello")
    
    def test_non_alpha_characters(self):
        self.assertEqual(caesarCipher("hello, world!", 5), "mjqqt, btwqi!")
    
    def test_numbers_in_string(self):
        self.assertEqual(caesarCipher("abc123", 2), "cde123")
    
    def test_thai_characters_not_equal(self):
        self.assertNotEqual(caesarCipher("กขค", 3), "กขค")
    
    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")
    
    def test_large_string(self):
        self.assertEqual(caesarCipher("The quick brown fox jumps over the lazy dog", 10), "Dro aesmu lbygx pyh tewzc yfob dro vkji nyq")
