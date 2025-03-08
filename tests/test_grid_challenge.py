from coe_6710110239.grid_challenge import gridChallenge
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")

    def test_unsorted_grid(self):
        self.assertEqual(gridChallenge(["cba", "daf", "ghi"]), "YES")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["zxc"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["z", "x", "c"]), "NO")

    def test_all_same_letters(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")

    def test_minimum_size_grid(self):
        self.assertEqual(gridChallenge(["a"]), "YES")

    def test_large_valid_grid(self):
        self.assertEqual(gridChallenge(["abcdef", "bcdefg", "cdefgh", "defghi"]), "YES")

    def test_large_invalid_grid(self):
        self.assertNotEqual(gridChallenge(["abcdef", "bcdfeg", "cdefgh", "defghi"]), "NO")

    def test_numbers_in_grid(self):
        self.assertEqual(gridChallenge(["123", "234", "345"]), "YES")

    def test_special_characters(self):
        self.assertEqual(gridChallenge(["!@#", "@#$", "#$%"]), "NO")

    def test_input_none(self):
        with self.assertRaises(TypeError):
            gridChallenge(None)

    def test_input_integer(self):
        with self.assertRaises(TypeError):
            gridChallenge(123)

    def test_input_list_of_integers(self):
        with self.assertRaises(TypeError):
            gridChallenge([123, 456, 789])

