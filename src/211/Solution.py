class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['end'] = True
    
    def search_rec(self, word: str, node: {}) -> bool:
        if not word:
            return 'end' in node
        c, *tail = word
        if c == '.':
            return any([self.search_rec(tail, node[k]) for k in node if k != 'end'])
        if c not in node:
            return False
        return self.search_rec(tail, node[c])
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_rec(word, self.trie)
        
       
        
            
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)