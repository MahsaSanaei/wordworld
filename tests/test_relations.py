import unittest
import sys
sys.path.append('.')
from wordword import WordGraph


class TestWordGraphMethods(unittest.TestCase):
    def setUp(self):
        self.wg = WordGraph()

    def test_add_rhyme(self):
        self.wg.add_rhyme('bad', 'sad')
        self.assertEqual(self.wg.G['bad']['sad']['relation'], 'rhymes_with')

    def test_add_synonym(self):
        self.wg.add_synonym('happy', 'joyful')
        self.assertEqual(self.wg.G['happy']['joyful']['relation'], 'synonym')

    def test_auto_connect_by_rhyme(self):
        words = ['cat', 'bat', 'car']
        self.wg.auto_connect_by_rhyme(words)
        self.assertEqual(self.wg.G['cat']['bat']['relation'], 'rhymes_with')

    def test_edit_distance(self):
        d2 = self.wg.edit_distance('cat', 'dog')
        self.assertEqual(d2, 3)

    def test_auto_connect_by_edit_distance(self):
        words = ['cat', 'bat', 'car']
        self.wg.auto_connect_by_edit_distance(words, max_distance=1)  
        self.assertIn('bat', self.wg.neighbors('cat'))  
        self.assertNotIn('car', self.wg.neighbors('bat'))  

    def test_word_path(self):
        words = ['cat', 'bat', 'bad']
        self.wg.auto_connect_by_edit_distance(words, max_distance=1)
        path = self.wg.word_path('cat', 'bad')
        self.assertEqual(path, ['cat', 'bat', 'bad'])

    def test_most_connected(self):
        self.wg.add_rhyme('a', 'b')
        self.wg.add_rhyme('a', 'c')
        self.wg.add_rhyme('a', 'd')
        top = self.wg.most_connected(1)
        self.assertEqual(top[0][0], 'a')


if __name__ == '__main__':
    unittest.main()
