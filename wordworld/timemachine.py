import requests
from pathlib import Path
import json
import time


CACHE_DIR = Path.home() / '.wordworld_cache'
CACHE_DIR.mkdir(exist_ok=True)

def load_cache(word):
    path = CACHE_DIR / f'{word}.json'
    if path.exists():
        content = path.read_text(encoding='utf-8')
        return json.loads(content) 
    return None

def save_cache(word, data):
    path = CACHE_DIR/f'{word}.json'
    path.write_text(json.dumps(data, indent=2))

def fetch_word(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else: return None
    except requests.ConnectionError:
        print('No internet connection')
        return None
    except requests.Timeout:
        print('Request timed out') 
        return None

def word_history(word):
    """
    Fetches full history dict for a word; caches to ~/.wordworld_cache/
    
    :param word
    """
    cached = load_cache(word)
    if cached:
        print('loaded from cache')
        return cached
    data = fetch_word(word)
    if data:
        save_cache(word, data)
    return data



def compare_words_history(words):
    """
    Fetches multiple words and returns comparison summary dict

    :param words
    """
    comparison_results = {}
    for word in words:
        clean_word = word.lower().strip()
        full_data = word_history(clean_word)
        if full_data:
            data_item = full_data[0]
            total_definitions = 0
            total_synonyms = 0
            
            meanings_list = data_item.get("meanings", [])
            
            for meaning in meanings_list:
                defs = meaning.get("definitions", [])
                total_definitions += len(defs)
                
                syns = meaning.get("synonyms", [])
                total_synonyms += len(syns)
            
            summary = {
                'definitions': total_definitions,
                'synonyms': total_synonyms
            }
            comparison_results[clean_word] = summary
        else:
            comparison_results[clean_word] = "Not Found"
        time.sleep(0.3) # wait 300ms between requests
    return comparison_results
