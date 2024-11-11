import unittest
from task2 import generate_variants, get_permutations_iteratively  # replace with actual module name

class TestPermutationFunctions(unittest.TestCase):

    def test_empty_string_recursive(self):
        """Test recursive function with an empty string."""
        result = generate_variants("", allow_repeats=True)
        self.assertEqual(result, [])

    def test_empty_string_iterative(self):
        """Test iterative function with an empty string."""
        result = get_permutations_iteratively("", allow_repeats=True)
        self.assertEqual(result, [])

    def test_single_character_recursive(self):
        """Test recursive function with a single character."""
        result = generate_variants("a", allow_repeats=True)
        self.assertEqual(result, ["a"])

    def test_single_character_iterative(self):
        """Test iterative function with a single character."""
        result = get_permutations_iteratively("a", allow_repeats=True)
        self.assertEqual(result, ["a"])

    def test_two_characters_recursive_with_duplicates(self):
        """Test recursive function with two characters allowing duplicates."""
        result = generate_variants("aa", allow_repeats=True)
        self.assertEqual(sorted(result), ["aa"])

    def test_two_characters_iterative_with_duplicates(self):
        """Test iterative function with two characters allowing duplicates."""
        result = get_permutations_iteratively("aa", allow_repeats=True)
        self.assertEqual(sorted(result), ["aa"])

    def test_two_characters_recursive_without_duplicates(self):
        """Test recursive function with two characters, no duplicates."""
        result = generate_variants("ab", allow_repeats=False)
        self.assertEqual(sorted(result), ["ab", "ba"])

    def test_two_characters_iterative_without_duplicates(self):
        """Test iterative function with two characters, no duplicates."""
        result = get_permutations_iteratively("ab", allow_repeats=False)
        self.assertEqual(sorted(result), ["ab", "ba"])

    def test_multiple_characters_recursive_with_duplicates(self):
        """Test recursive function with multiple characters allowing duplicates."""
        result = generate_variants("abc", allow_repeats=True)
        self.assertEqual(sorted(result), ["abc", "acb", "bac", "bca", "cab", "cba"])

    def test_multiple_characters_iterative_with_duplicates(self):
        """Test iterative function with multiple characters allowing duplicates."""
        result = get_permutations_iteratively("abc", allow_repeats=True)
        self.assertEqual(sorted(result), ["abc", "acb", "bac", "bca", "cab", "cba"])

