import unittest
import sys
sys.path.append('.')
from wordword import Corpus


class TestCorpusMethods(unittest.TestCase):
    def setUp(self):
        self.corp = Corpus("To be or not to be, That is the question.")

    def test_most_common(self):
        result = self.corp.most_common(2)
        self.assertEqual(result, [('to', 2), ('be', 2)])

    def test_rarest_words(self):
        result = self.corp.rarest_words(2)
        self.assertEqual(result, [('question', 1), ('the', 1)])

    def test_lexical_diversity(self):
        result = self.corp.lexical_diversity()
        self.assertEqual(result, 0.8)

    def test_avg_word_length(self):
        result = self.corp.avg_word_length()
        self.assertEqual(result, 3.0)
    
    def test_avg_sentence_length(self):
        result = self.corp.avg_sentence_length()
        self.assertEqual(result, 10.0)

    def test_rarity_score(self):
        result = self.corp.rarity_score('be')
        self.assertEqual(result, 0.8)

    def test_fingerprint(self):
        result = self.corp.fingerprint()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['unique_words'], 8)
        self.assertEqual(result['avg_word_length'], 3.0)


if __name__ == '__main__':
    unittest.main()
