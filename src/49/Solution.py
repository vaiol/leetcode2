from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr = [''.join(sorted(s)) for s in strs]
        setSortedStr = list(set(sortedStr))
        anagrams = [[] for _ in range(len(setSortedStr))]
        for i in range(len(strs)):
            index = setSortedStr.index(sortedStr[i])
            anagrams[index].append(strs[i])
        return anagrams
