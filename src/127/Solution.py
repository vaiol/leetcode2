class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = [beginWord] + wordList
        key_words_dict = defaultdict(set)
        word_keys_dict = defaultdict(set)
        word_words_dict = defaultdict(set)

        for word in words:
            for i in range(len(word)):
                l = list(word)
                l[i] = '*'
                key = ''.join(l)
                key_words_dict[key].add(word)
                word_keys_dict[word].add(key)

        for word, keys in word_keys_dict.items():
            words = set()
            for key in keys:
                words.update(key_words_dict[key])
            words.remove(word)
            word_words_dict[word] = words

        queue = deque()
        visited = set()
        queue.append((endWord, 1))
        visited.add(endWord)
        while queue:
            word, level = queue.popleft()
            if word == beginWord:
                return level
            for ref_word in word_words_dict[word]:
                if ref_word not in visited:
                    queue.append((ref_word, level + 1))
                    visited.add(ref_word)
        return 0