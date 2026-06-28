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


### 3.1 Stage 1: Word Inspector
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
# {'syllables': 2, 'chars': {'upper': 1, 'lower': 5, 'digits': 1, ...}, 'palindrome': False}
```
