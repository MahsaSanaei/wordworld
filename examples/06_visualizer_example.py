import sys
sys.path.append('.')
from wordword import plot_word_frequency, plot_personality_radar, plot_sentence_length_distribution, compare_texts_visually


text = "Hello, I love you so much. According to my feelings to you, I always support you."
plot_word_frequency(text, 3)
plot_personality_radar(text)
plot_sentence_length_distribution(text)
compare_texts_visually({
    "Hafez": "بیت‌های حافظ...",
    "Saadi": "متنی از سعدی...",
    "Your Text": "Here is some English text..."
    })
