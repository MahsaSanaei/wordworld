import networkx as nx


class WordGraph:
    def __init__(self):
        self.G = nx.Graph()
        
    def add_rhyme(self, word1, word2):
        """
        Adds an edge with relation='rhymes_with'
        
        :param self 
        :param word1 
        :param word2 
        """
        self.G.add_edge(word1, word2, relation='rhymes_with')

    def add_synonym(self, word1, word2):
        """
        Adds an edge with relation='synonym'
        
        :param self
        :param word1
        :param word2 
        """
        self.G.add_edge(word1, word2, relation='synonym')
    
    def auto_connect_by_rhyme(self, words):
        """
        Scans a word list, auto-adds rhyme edges
        
        :param self 
        :param words 
        """
        for i in range(len(words)-1):
            self.G.add_edge(words[i], words[i+1], relation='rhymes_with')

    def edit_distance(self, w1, w2):
        """
        Returns integer Levenshtein distance between two words
        
        :param self
        :param w1
        :param w2 
        """
        m,n = len(w1), len(w2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1): dp[i][0] = i  # cost to delete all of w1 
        for j in range(n+1): dp[0][j] = j  # cost to insert all of w2

        for i in range(1, m+1):
            for j in range(1, n+1):
                if w1[i-1] == w2[j-1]:  # characters match
                    dp[i][j] = dp[i-1][j-1]  # free
                
                else:
                    dp[i][j] = 1 + min(
                    dp[i-1][j],  # delete
                    dp[i][j-1],  # insert
                    dp[i-1][j-1]  # replace
                    ) 
        
        return dp[m][n]
    
    def auto_connect_by_edit_distance(self, words, max_distance=1):
        """
        Auto-adds edges for words differing by ≤N chars
        
        :param self
        :param words
        :param max_distance
        """
        for i, w1 in enumerate(words):
            for w2 in words[i+1:]:  # avoid checking same pair twice
                if self.edit_distance(w1,w2) <= max_distance: 
                    self.G.add_edge(w1, w2)
        return self.G

    def neighbors(self, word):
        """
        Returns list of all words connected to given word

        :param self
        :param word 
        """
        return list(self.G.neighbors(word))
    
    def word_path(self, start, end):
        """
        BFS shortest path between two words

        :param self 
        :param start 
        :param end        
        """
        try:
            path = nx.shortest_path(self.G, start, end)
        except nx.NetworkXNoPath:
            print('No path found')
        return path
    
    def most_connected(self, n):
        """
        Returns top-n most connected (highest degree) words

        :param self 
        :param n
        """
        degrees = self.G.degree()
        sorted_nodes = sorted(degrees, key=lambda x: x[1], reverse=True)
        return [node for node, deg in sorted_nodes[:n]]
