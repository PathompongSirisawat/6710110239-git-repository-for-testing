from coe_6710110239.alternating_characters import alternating_characters

import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_characters_A(self):
        self.assertEqual(alternating_characters("AAAA"), 3)

    def test_all_same_characters_B(self):
        self.assertEqual(alternating_characters("BBBBB"), 4)

    def test_perfect_alternating_AB(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)

    def test_perfect_alternating_BA(self):
        self.assertEqual(alternating_characters("BABABA"), 0)

    def test_consecutive_repetitions_A_then_B(self):
        self.assertEqual(alternating_characters("AAABBB"), 4)

    def test_single_character(self):
        self.assertEqual(alternating_characters("A"), 0)

    def test_two_different_characters(self):
        self.assertEqual(alternating_characters("AB"), 0)

    def test_mixed_repetitions(self):
        self.assertEqual(alternating_characters("ABBABB"), 2)

    def test_leading_repetitions_then_mixed(self):
        self.assertEqual(alternating_characters("BBBBBAAB"), 5)

    def test_grouped_repetitions(self):
        self.assertEqual(alternating_characters("AABBAABB"), 4)
    
    def test_long_string_with_mixed_patterns(self):
        self.assertEqual(alternating_characters("AABBABAABBBABABABAAA"), 7)

    def test_alternating_with_one_extra(self):
        self.assertEqual(alternating_characters("ABABABAABB"), 2)

    def test_no_redundant_deletions_needed(self):
        self.assertEqual(alternating_characters("BAABAB"), 1)

    def test_thai_characters(self):
        self.assertEqual(alternating_characters("กกกกขขขข"), 6)
    
    def test_mixed_alphabet_and_numbers(self):
        self.assertEqual(alternating_characters("A1A1B2B2"), 0)
    
    def test_numbers_only(self):
        self.assertEqual(alternating_characters("11112222"), 6)
    
    def test_invalid_characters(self):
        self.assertEqual(alternating_characters("A@B#C$"), 0)
    
    def test_empty_string(self):
        self.assertEqual(alternating_characters(""), 0)
    
    def test_none_input(self):
        with self.assertRaises(TypeError):
            alternating_characters(None)
