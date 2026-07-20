import unittest
from unittest.mock import patch
import re
import sys
sys.path.append('.')
from wordworld import word_history, compare_words_history


class TestTimeMachinehMethods(unittest.TestCase):
    @patch('timemachine.word_history')
    def test_compare_words_history(self, mock_word_history):
        mock_word_history.return_value = [
            {
                "word": "love",
                "meanings": [
                    {
                        "definitions": [{}, {}, {}], # 3 definitions
                        "synonyms": [{}, {}]         # 2 synonyms
                    },
                    {
                        "definitions": [{}],        # 1 definition
                        "synonyms": []               # 0 synonyms
                    }
                ]
            }
        ]
        words = ["love"]
        result = compare_words_history(words)

        expected_summary = {'definitions': 4, 'synonyms': 2}
        
        self.assertIn("love", result)
        self.assertEqual(result["love"], expected_summary)

    @patch('timemachine.word_history')
    def test_compare_words_words_not_found(self, mock_word_history):
        
        mock_word_history.return_value = [] 

        words = ["unknown"]
        result = compare_words_history(words)

        self.assertEqual(result["unknown"], "Not Found")


if __name__ == '__main__':
    unittest.main()
    