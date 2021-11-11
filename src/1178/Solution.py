from typing import List, Counter


class Solution:
    def findNumOfValidWords1(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 09.11.2021 Time Limit Exceeded
        ans = [0] * len(puzzles)

        words_set = Counter()

        for i, word in enumerate(words):
            words_set[frozenset(word)] += 1

        for i, puzzle in enumerate(puzzles):
            puzzle_set = set(puzzle)
            for j, word_set in enumerate(words_set):
                if word_set.issubset(puzzle_set) and puzzles[i][0] in word_set:
                    ans[i] += words_set[word_set]
        
        return ans
