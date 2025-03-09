from coe_6710110239.CatandMouse import CatandMouse

import unittest


class CatAndMouseTest(unittest.TestCase):
    def test_mouse_c_wins(self):
        result = CatandMouse(1, 3, 2)
        self.assertEqual(result, "Mouse C")

    def test_cat_b_wins(self):
        result = CatandMouse(2, 5, 4)
        self.assertEqual(result, "Cat B")
    
    def test_mouse_escapes(self):
        result = CatandMouse(1, 5, 3)
        self.assertEqual(result, "Mouse C")
    
    def test_cat_a_closer(self):
        result = CatandMouse(0, 4, 1)
        self.assertEqual(result, "Cat A")
    
    def test_cat_b_closer(self):
        result = CatandMouse(3, 6, 5)
        self.assertEqual(result, "Cat B")
    
    def test_equal_distance_mouse_wins(self):
        result = CatandMouse(2, 6, 4)
        self.assertEqual(result, "Mouse C")
    
    def test_negative_positions(self):
        result = CatandMouse(-3, -1, -2)
        self.assertEqual(result, "Mouse C")
    
    def test_large_numbers(self):
        result = CatandMouse(1000000, 5000000, 3000000)
        self.assertEqual(result, "Mouse C")
    
    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            CatandMouse("a", 3, 2)
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            CatandMouse(None, 3, 2)