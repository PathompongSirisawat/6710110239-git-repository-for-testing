from coe_6710110239.Staircase import staircase

import unittest

class StaircaseTest(unittest.TestCase):
    def test_staircase_height_1(self):
        self.assertEqual(staircase(1), "#\n")
    
    def test_staircase_height_3(self):
        expected = "  #\n ##\n###\n"
        self.assertEqual(staircase(3), expected)
    
    def test_staircase_height_5(self):
        expected = "    #\n   ##\n  ###\n ####\n#####\n"
        self.assertEqual(staircase(5), expected)
    
    def test_staircase_custom_pattern(self):
        expected = "  @\n @@\n@@@\n"
        self.assertEqual(staircase(3, "@"), expected)
    
    def test_staircase_height_0(self):
        self.assertEqual(staircase(0), "")
    
    def test_staircase_negative_height(self):
        self.assertEqual(staircase(-3), "")
    
    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            staircase("five")
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            staircase(None)
