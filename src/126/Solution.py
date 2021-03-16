class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = [beginWord] + wordList
        key_words = defaultdict(set)
        word_keys = defaultdict(set)
        
        for word in words:
            for i in range(len(word)):
                l = list(word)
                l[i] = '*'
                key = ''.join(l)
                key_words[key].add(word)
                word_keys[word].add(key)
        
        word_words = defaultdict(set)
        for word in words:
            for key in word_keys[word]:
                word_words[word].update(key_words[key])
            word_words[word].remove(word)
        
        ans = []
        queue = deque()
        queue.append((beginWord, [beginWord]))
        visited = set(beginWord)
        
        while queue and not ans:
            queue_len = len(queue)
            local_visited = set()
            for _ in range(queue_len):
                word, path = queue.popleft()
                for child_word in word_words[word]:
                    if child_word == endWord:
                        ans.append(path + [child_word])
                    if child_word not in visited:
                        queue.append((child_word, path + [child_word]))
                        local_visited.add(child_word)
            visited.update(local_visited)
        return ans
        