class ResultNode:
    def __init__(self, word: str, priority: int):
        self.word = word;
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority if self.priority != other.priority else self.word > other.word

class Trie:
    def __init__(self):
        self.head = dict()
        self.result = []
        self.input = ""
        self.currHead = self.head
        

    def add(self, word: str, hot = 1) -> None:
        curr = self.head
        for c in word:
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        if '#' in curr:
            curr['#'] += hot
        else:
            curr['#'] = hot

    def getAll(self, head: dict, word: str) -> List[str]:
        if '#' in head:
            # if len(self.result) >= 3:
            #     heappushpop(self.result, ResultNode(word, head['#']))
            # else:
            #     heappush(self.result, ResultNode(word, head['#']))
            heappush(self.result, ResultNode(word, head['#']))
            
        for k in head:
            if k != '#':
                self.getAll(head[k], word + k)

    def addChar(self, ch: str) -> List[str]:
        self.input += ch
        
        if ch == '#':
            if ch not in self.currHead:
                self.currHead[ch] = 0
            self.currHead[ch] += 1
            self.currHead = self.head
            self.input = ""
            return []
        
        if ch not in self.currHead:
            self.currHead[ch] = dict()
            
        self.currHead = self.currHead[ch]

        self.result = []
        self.getAll(self.currHead, self.input)
        return self.result
        

        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.add(sentences[i], times[i])
        

    def input(self, c: str) -> List[str]:
        res = self.trie.addChar(c)
        return [node.word for node in nlargest(3, res)]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)