import sys
sys.path.append('.')
from wordword import WordGraph

wg = WordGraph()
wg.add_rhyme('cat', 'bat')
wg.add_synonym('pod', 'sod')

words = ['cat','bat','bad','bed','red','rod','dog']
wg.auto_connect_by_rhyme(words)
print(wg.edit_distance("kitten", "sitting"))
print(wg.edit_distance("cat", "cat"))

ed = wg.auto_connect_by_edit_distance(words, max_distance=1)
print(ed)
print(wg.neighbors('cat'))
print(wg.word_path('cat', 'bad'))
print(wg.most_connected(2))
