import matplotlib.pyplot as plt
import numpy as np
import re
import math
from .corpus import Corpus
from .personality import score_personality


def plot_word_frequency(text, top_n):
    """
    Horizontal bar chart of top-N most frequent words
    
    :param text
    :param top_n
    """
    corpus = Corpus(text)
    common_words = corpus.most_common(top_n)
    #print(common_words)

    words = [w for w,c in common_words]
    counts = [c for w,c in common_words]

    plt.figure(figsize=(8,4))
    plt.barh(words, counts, color="#7CA84C")
    plt.ylabel("Frequency")
    plt.title("Top word frequencies")
    plt.show()


def plot_personality_radar(text, title="Personality Radar"):
    """
    Polar/radar chart of the 5 personality dimensions
    
    :param text
    :param title
    """
    result = score_personality(text)
    labels = ["Formality", "Complexity", "Emotionality", "Rhythm", "Richness"]
    values = [
        result.formality,
        result.complexity,
        result.emotionality,
        result.rhythm,
        result.richness
    ]
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_ylim(0, 1)

    plt.title(title, y=1.08)
    plt.show()


def plot_sentence_length_distribution(text):
    """
    Histogram + line chart showing rhythm over time
    
    :param text
    """
    result = score_personality(text)
    rhythm_score = result.rhythm

    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_lengths = [len(s.split()) for s in sentences]

    if not sentence_lengths:
        print("Text has no sentences.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    counts, bins, patches = ax.hist(
        sentence_lengths,
        bins=range(0, max(sentence_lengths) + 1, 2),
        color="#87CEFA",
        alpha=0.6,
        label="Sentence length distribution"
    )

    ax.plot(bins[:-1], counts, color="#1E90FF", linewidth=2, label="Rhythm pattern")

    ax.set_xlabel("Sentence length (words)")
    ax.set_ylabel("Frequency")
    plt.title(f"Rhythm score: {rhythm_score:.3f}", fontsize=12, weight="bold")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()


def compare_texts_visually(texts_dict):
    """
    Side-by-side radar charts for multiple texts/authors.
    
    :param texts_dict: dict -> {"Author Name": "text ..."}
    """
    labels = ["Formality", "Complexity", "Emotionality", "Rhythm", "Richness"]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    authors = list(texts_dict.keys())
    n = len(authors)

    cols = min(n, 3)
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols, subplot_kw=dict(polar=True), figsize=(5 * cols, 5 * rows))

    if n == 1:
        axes = np.array([[axes]])
    elif rows == 1:
        axes = np.array([axes])

    idx = 0

    for r in range(rows):
        for c in range(cols):

            if idx >= n:
                axes[r, c].axis("off")
                continue

            author = authors[idx]
            text = texts_dict[author]

            result = score_personality(text)
            values = [
                result.formality,
                result.complexity,
                result.emotionality,
                result.rhythm,
                result.richness
            ]
            values += values[:1]

            ax = axes[r, c]
            ax.plot(angles, values, linewidth=2)
            ax.fill(angles, values, alpha=0.25)

            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels)

            ax.set_ylim(0, 1)
            ax.set_title(author, y=1.10, fontsize=13, fontweight="bold")

            idx += 1

    plt.tight_layout()
    plt.show()
