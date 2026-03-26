from collections import Counter
import os


class Corpus:
    #STOPWORDS=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 
    #       'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
    #       'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 
    #       'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 
    #       'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 
    #       'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
    #       'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 
    #       'will', 'just', 'don', 'should', 'now']
    
    PUNC = """!()-[]{};:```\\`'//'"``\`,<>./?@#$%^&*_~1234567890=\n\t|"""

    def __init__(self, data):
        if os.path.isfile("data") and "data".endswith(".txt"):
            with open ("data", "r") as f:
                self.raw_data = f.read()
        else:
            self.raw_data = data
        
        raww_data =  self.raw_data.lower()
        for ele in raww_data:
            if ele in self.PUNC:
                raww_data = raww_data.replace(ele, " ")
        words = raww_data.split()
        #words = [word for word in words if word not in self.STOPWORDS]    #stopword removal
        self.words_freq = Counter(words)

    def most_common(self, n): 
        """
        Returns top-n (word, count) pairs as a list of tuples

        :param n
        """
        return self.words_freq.most_common(n)

    def rarest_words(self, n):
        """
        Returns the n least frequent words in the corpus

        :param n
        """
        ordered_word_freq = self.words_freq.most_common()
        ordered_word_freq = list(reversed(ordered_word_freq))
        return ordered_word_freq[:n]
