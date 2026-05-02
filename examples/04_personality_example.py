import sys
sys.path.append('.')
from wordword import score_personality


text = "Hello, I love you so much. According to my feelings to you, I always support you."
result = score_personality(text)
print(result) 
