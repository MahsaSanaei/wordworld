import sys
sys.path.append('.')
import wordworld as ww


result = ww.word_history("serendipity")
if result:
    data = result[0] 
    print(f"Word: {data.get('word')}")
    print(f"Phonetic: {data.get('phonetic')}") 
    meanings = data.get('meanings', [])
    first_meaning = meanings[0]['definitions'][0]['definition']
    print(f"First Definition: {first_meaning}")

words = ['love','hate', 'serendipity']
result = ww.compare_words_history(words)
for w, stats in result.items():
    print(w, stats)
    