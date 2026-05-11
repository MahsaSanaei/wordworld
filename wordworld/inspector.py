
from collections import Counter


def count_syllables(word):
    """
    Returns integer count of syllables using vowel-group detection
    
    :param word
    """
    word = word.lower()
    vowels = 'aeiouy' # y can be a vowel sound 
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel: 
            count += 1 
        prev_was_vowel = is_vowel
    if word.endswith('e') and count > 1: 
        count -= 1

    return max(0, count)

def classify_chars(word):
    """
    Returns dict counting uppercase, lowercase, digits, special chars
    
    :param word
    """
    counts = {'uppercase':0, 'lowercase':0, 'digits':0 , 'special':0}
    for char in word:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['special'] += 1

    return counts

def is_palindrome(word):
    """
    Returns True/False — whether word reads same forwards and backwards

    :param word
    """
    word = word.lower() if len(word) > 0 else 'False'
    return word == word[::-1]

def inspect(word):
    """
    Master function — returns a dict with all properties of a word
    
    :param word
    """
    char_types = classify_chars(word)
    lower_word = word.lower() 
    vowels = 'aeiou'
    vowel_count, consonant_count = 0, 0
    for char in lower_word:
        if char.isalpha() and char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    return {
        'word': word,
        'length': len(lower_word),
        'syllable_count': count_syllables(lower_word),
        'start_with_vowel':'True' if len(lower_word)>0 and lower_word[0] in vowels else 'False',
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'is_palindrome': is_palindrome(lower_word),
        'char_types': char_types,
        'unique_letters': len(set(lower_word)),
        'letter_freq': dict(Counter(lower_word))
        }
