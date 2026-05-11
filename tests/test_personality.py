import unittest
import re
import sys
sys.path.append('.')
from wordworld import TextPersonality, score_personality


class TestPersonalityhMethods(unittest.TestCase):

    def setUp(self):
        """
        This method runs before each test. Use it to define the input text and its 
        corresponding scores.
        """
        self.text1 = "Test text for richness and casual profile."
        self.scores1 = score_personality(self.text1)
        formality1 = self.scores1.formality
        complexity1 = self.scores1.complexity
        emotionality1 = self.scores1.emotionality
        rhythm1 = self.scores1.rhythm
        richness1 = self.scores1.richness
        self.personality1 = TextPersonality(formality1, complexity1, emotionality1, rhythm1, richness1)

        self.text2 = "An academic paper discussing complex theories, delving into intricate concepts " \
        "and their interrelationships. This research aims to provide a comprehensive analysis," \
        "exploring the nuances and implications of these sophisticated ideas for a scholarly audience."
        self.scores2 = score_personality(self.text2)
        formality2 = self.scores2.formality
        complexity2 = self.scores2.complexity
        emotionality2 = self.scores2.emotionality
        rhythm2 = self.scores2.rhythm
        richness2 = self.scores2.richness
        self.personality2 = TextPersonality(formality2, complexity2, emotionality2, rhythm2, richness2)
        
    def test_dominant_trait(self):
        self.assertEqual(self.personality1.dominant_trait(), "rhythm")
        self.assertEqual(self.personality2.dominant_trait(), "richness")

    def test_profile_label(self):
        self.assertEqual(self.personality1.profile_label(), "Casual / Conversational")
        self.assertEqual(self.personality2.profile_label(), "Balanced / Neutral")

    def test_str_output_format_casual(self):
        output = str(self.personality1)
        self.assertIn(f"Dominant trait: {self.personality1.dominant_trait()}", output)
        self.assertIn(f"Profile: {self.personality1.profile_label()}", output)


if __name__ == '__main__':
    unittest.main()
