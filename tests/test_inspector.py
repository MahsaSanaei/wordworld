import unittest
import sys
sys.path.append('.')
from wordword import inspect, count_syllables, classify_chars, is_palindrome


class TestInspectorMethods(unittest.TestCase):
    def test_inspect(self):
        result = inspect("HEllo123@!")
        self.assertIsInstance(result, dict)
        self.assertEqual(result['length'], 10)
        self.assertEqual(result['syllable_count'], 2)

    def test_classify_chars(self):
        result = classify_chars("Butter")
        self.assertIsInstance(result, dict)
        self.assertEqual(result['uppercase'],1)
        self.assertEqual(result['digits'], 0)

    def test_count_syllables(self):
        self.assertEqual(count_syllables("cat"), 1)
        self.assertEqual(count_syllables("serendipity"), 5)

    def test_palindromes(self):
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertEqual(is_palindrome("hello"), False)

    def test_empty_word(self):
        result = inspect("")
        self.assertEqual(result["length"], 0)


if __name__ == '__main__':
    unittest.main()
