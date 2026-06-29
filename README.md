# WordWorld (A Living Word Intelligence Library)

## 1. Project Overview
wordworld is a Python library that lets you inspect, analyze, compare, and visualize text and words at many levels — from individual characters up to full documents. It is designed for beginner programmers who want to build something real and publishable while learning core Python engineering skills step by step.

## 2. Project Structure
Every file in wordworld has exactly one responsibility. Here is the complete directory layout:

```
wordworld/ 
├── wordworld/
│ ├── __init__.py           ← Public API exports (imports from all modules)
│ ├── inspector.py          ← Stage 1: Single-word analysis
│ ├── corpus.py             ← Stage 2: Multi-word / document analysis
│ ├── relations.py          ← Stage 3: Word graphs & relationships
│ ├── personality.py        ← Stage 4: Text style & personality scoring
│ ├── timemachine.py        ← Stage 5: API calls, etymology, caching
│ ├── visualizer.py         ← Stage 6: All matplotlib charts
│ └── cli.py                ← Stage 7: Terminal command-line interface
├── tests/
│ ├── test_inspector.py
│ ├── test_corpus.py
│ ├── test_relations.py
│ └── test_personality.py
├── examples/
│ ├── compare_authors.py
│ ├── analyze_news.py
│ └── word_game.py
├── pyproject.toml          ← Package metadata & dependencies
├── README.md
└── CHANGELOG.md
```

## 3. Project Roadmap

| File / Folder | Stage | Responsibility |
| :--- | :---: | :--- |
| **wordworld/__init__.py** | All stages | Re-exports everything for clean imports |
| **wordworld/inspector.py** | Stage 1 | Pure functions on a single word string |
| **wordworld/corpus.py** | Stage 2 | Corpus class — statistics over many words |
| **wordworld/relations.py** | Stage 3 | WordGraph class — networkx-based word graph |
| **wordworld/personality.py** | Stage 4 | TextPersonality dataclass + score_personality() |
| **wordworld/timemachine.py** | Stage 5 | HTTP + JSON + disk cache for word history |
| **wordworld/visualizer.py** | Stage 6 | All matplotlib/plotting functions |
| **wordworld/cli.py** | Stage 7 | click commands: info, analyze, personality, history |
| **tests/** | All stages | pytest unit tests, one file per module |
| **examples/** | All stages | Runnable demo scripts for users |

“This project is an evolving library. Feel free to explore the modules and contribute as you learn!”


### 3.1. Stage 1: Word Inspector
This module contains pure functions (no classes) that take a single word string and return facts about it. This is intentionally the simplest possible design pattern to get started.

| Function / Method | Description |
| :--- | :--- |
| `inspect(word)` | **Master function** — Returns a dictionary containing all analyzed properties of the word. |
| `count_syllables(word)` | Returns the integer count of syllables using vowel-group detection. |
| `classify_chars(word)` | Returns a dictionary with counts for uppercase letters, lowercase letters, digits, and special characters. |
| `is_palindrome(word)` | Returns `True` or `False` — determines if the word reads the same forwards and backwards. |

#### Usage Example
```python
from wordworld.inspector import inspect

data = inspect("Python3")
print(data)
# Output example:
# {'word': Python3, 'length':7, 'syllable_count': 2, 'char_types': {'uppercase': 1, 'lowercase': 5, 'digits': 1, ...}, 'is_palindrome': False, ...}
```


### 3.2. Stage 2: Corpus Analyzer
The Corpus class wraps a block of text (string or file path) and exposes statistical methods.

| Function / Method | Description |
| :--- | :--- |
| `Corpus(source)` | Constructor — accepts a raw string or a file path |
| `most_common(n)` | Returns top-n (word, count) pairs as a list of tuples |
| `rarest_words(n)` | Returns the n least frequent words in the corpus |
| `lexical_diversity()` | Returns float 0–1: unique words / total words (TTR) |
| `avg_word_length()` | Returns the average number of characters per word |
| `avg_sentence_length()` | Returns the average number of words per sentence |
| `rarity_score(word)` | Returns 0–1 float: how rare a specific word is in this corpus |
| `fingerprint()` | Returns summary dict with all key statistics combined |

#### Usage Example
```python
from wordworld.corpus import fingerprint

c = Corpus("To be or not to be, That is the question.")
c.fingerprint()
# Output example:
# {'total_words': 10, 'unique_words':9, 'lexical_diversity': 0.90, 'avg_word_length': 3.2, 'avg_sentence_len': 10.2, 'top_5_words': [('be',2),...]}
```

### 3.3. Stage 3: Word Relationship Map
The WordGraph class builds a graph where words are nodes and relationships are edges.

| Function / Method | Description |
| :--- | :--- |
| `WordGraph()` | Constructor — creates an empty networkx Graph |
| `.add_rhyme(word1, word2)` | Adds an edge with relation='rhymes_with' |
| `.add_synonym(word1, word2)` | Adds an edge with relation='synonym' |
| `.auto_connect_by_rhyme(wo rds)` | Scans a word list, auto-adds rhyme edges |
| `.auto_connect_by_edit_dis tance()` | Auto-adds edges for words differing by ≤N chars |
| `.neighbors(word)` | Returns list of all words connected to given word |
| `.word_path(start, end)` | BFS shortest path between two words |
| `.most_connected(n)` | Returns top-n most connected (highest degree) words |
| `.edit_distance(w1, w2)` | Returns integer Levenshtein distance between two words |

#### Usage Example
```python
from wordworld.relations import WordGraph

wg = WordGraph()
words = ["cat","bat","rat"]
wg.neighbors("cat")
wg.edit_distance("cat", "cat")
# Output example:
# ['bat', 'rat', 'hat']
# 0
```

### 3.4. Stage 4: Text Personality Scorer
This module scores five personality dimensions of any text — formality, complexity, emotionality, rhythm, and richness — using purely statistical methods.

| Function / Method | Description |
| :--- | :--- |
| `TextPersonality` | Dataclass with 5 float fields (0.0–1.0 each) |
| `.dominant_trait()` | Returns the name of the highest-scoring trait |
| `.profile_label()` | Returns human label like 'Academic/Legal', 'Poetic' |
| `.__str__()` | Prints a bar-chart style personality report to terminal |
| `score_personality(text)` | Main function — returns a TextPersonality for any string |

#### Usage Example
```python
from wordworld.personality import score_personality
from wordworld.corpus import Corpus

text = Corpus(text)
p = score_personality(text) 
print(p.formality)
print(p.dominant_trait())
# Output example:
# 0.21
# 'rhythm'
```

### 3.5. Stage 5: Word History & Etymology


### 3.6. Stage 6: Visual Word Explorer


### 3.7. Stage 7: Command-Line Interface
