from dataclasses import dataclass
from .corpus import Corpus
from .inspector import count_syllables
import statistics


@dataclass
class TextPersonality:
    formality:  float
    complexity:  float
    emotionality:  float
    rhythm:  float
    richness:  float

    def dominant_trait(self):
        traits = {
            'formality': self.formality,
            'complexity': self.complexity,
            'emotionality': self.emotionality,
            'rhythm': self.rhythm,
            'richness': self.richness
        }
        return max(traits, key=traits.get)
    
    def profile_label(self):
        if self.formality > 0.7 and self.complexity > 0.6:
            return "Academic / Legal"
        elif self.emotionality > 0.7 and self.rhythm > 0.6:
            return "Poetic / Rhythmic"
        elif self.formality < 0.4 and self.emotionality < 0.5:
            return "Casual / Conversational"
        else:
            return "Balanced / Neutral"
        
    def __str__(self):
        result = [
            "Text Personality Report",
            "-----------------------------------",
            f"Formality       {self.formality:.3f}",
            f"Complexity      {self.complexity:.3f}",
            f"Emotionality    {self.emotionality:.3f}",
            f"Rhythm          {self.rhythm:.3f}",
            f"Richness        {self.richness:.3f}",
            "-----------------------------------",
            f"Profile: {self.profile_label()}",
            f"Dominant trait: {self.dominant_trait()}"
        ]
        return "\n".join(result)


FORMAL_WORDS = {
    "therefore", "however", "moreover", "consequently", "furthermore",    
    "consequently", "hence", "thus", "nevertheless", "nonetheless", 
    "whereas", "provided that", "assuming that", "in order to", "accordingly",     
    "subsequently", "substantive", "substantiate", "substantiation", "ostensibly",     
    "pertinent", "subordinate", "discrepancy", "prevalence", "substantiate", 
    "ubiquitous",      
}

def compute_formality(corpus, total_words):
    """
    Dimension 1 — Formality (0=casual, 1=formal)
    Formal writing uses longer Latinate words and specific formal-marker phrases. 
    Casual writing uses short common words and contractions.

    :param corpus
    :param total_words
    """
    formal_word_count = sum(1 for word in total_words if word in FORMAL_WORDS)
    formal_ratio = formal_word_count / len(total_words) if total_words else 0.0
    
    avg_len = corpus.avg_word_length()
    length_score = avg_len / 8.0 
    
    formality = (formal_ratio * 3 + length_score) / 2 
    
    return min(1.0, formality)


def compute_complexity(unique_words, total_words, sentences):
    """
    Dimension 2 — Complexity (0=simple, 1=complex)
    Complexity measures how hard the vocabulary and sentence structure is. Long sentences
    with multi-syllable words = high complexity.

    :param unique_words
    :param total_words
    :param sentences
    """
    avg_syllables = sum(count_syllables(w) for w in unique_words) / len(total_words )
    syllable_score = min(avg_syllables / 3.0, 1.0)
    # avg of sentence length
    avg_sent_len = len(total_words) / len(sentences) 
    sent_score = min(avg_sent_len / 25.0, 1.0)
    complexity = (syllable_score + sent_score) / 2
    return complexity


EMOTIONAL_WORDS = {
    "love", "hate", "fear", "joy", "anger", "sadness", "happiness",
    "furious", "ecstatic", "terrified", "horrified", "elated",
    "despair", "grief", "rage", "bliss",

    "wonderful", "amazing", "terrible", "awful", "fantastic",
    "gorgeous", "dreadful", "lovely", "annoyed", "pleased",
    "anxious", "excited", "calm", "content",

    "beautiful", "ugly", "good", "bad", "great", "poor",
    "success", "failure", "victory", "defeat", "hope", "disappointment",
    "surprise", "shock", "trust", "betrayal", "passion", "apathy",
}

def compute_emotionality(unique_words, total_words):
    """
    Dimension 3 — Emotionality (0=neutral, 1=emotional)

    Measures whether the text is charged with feeling versus dry and factual.
    emotionality = min(emotional_ratio * 20, 1.0)

    :param unique_words
    :param total_words
    """
    if not unique_words or total_words == 0:
        return 0.0

    emotional_count = sum(
        1 for word in unique_words
        if word.lower() in EMOTIONAL_WORDS
    )

    emotional_ratio = emotional_count / len(total_words)
    emotionality = min(emotional_ratio * 20.0, 1.0)

    return round(emotionality, 3)


def compute_rhythm(sentences):
    """
    Dimension 4 — Rhythm (0=chaotic, 1=very rhythmic)

    Rhythmic writing has consistent sentence lengths. We measure how much sentence lengths vary from the average using standard deviation.
    rhythm = max(0.0, 1.0 - std_dev / 10.0)

    :param sentences
    """
    
    if not sentences:
        return 0.0

    lengths = [len(s.split()) for s in sentences]

    if not lengths:
        return 0.0
        
    # If there's only one sentence, standard deviation is 0.
    if len(lengths) < 2:
        std_dev = 0.0
    else:
        std_dev = statistics.stdev(lengths)

    rhythm = max(0.0, 1.0 - std_dev / 10.0)
    
    return round(rhythm, 3)


def score_personality(text):
    corpus = Corpus(text)
    unique_words = corpus.unique_words
    total_words = corpus.total_words
    sentences = corpus.sentences
      
    formality = compute_formality(corpus, total_words)
    complexity = compute_complexity(unique_words, total_words, sentences) 
    emotionality = compute_emotionality(unique_words, total_words)
    rhythm = compute_rhythm(sentences)
    richness = corpus.lexical_diversity()
    return TextPersonality(formality, complexity, emotionality, rhythm, richness)
