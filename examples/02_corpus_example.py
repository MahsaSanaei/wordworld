import sys
sys.path.append('.')
from wordworld import Corpus

corp = Corpus("Hello world. How are you? I am fine.")
print(corp.most_common(2))
print(corp.fingerprint())
