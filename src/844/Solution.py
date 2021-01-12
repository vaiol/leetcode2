import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def rem(S: str) -> str:
            counter = 0
            for n in reversed(S):
                if n == '#':
                    counter += 1
                elif counter:
                    counter -= 1
                else:
                    yield n
        return all(x == y for x,y in itertools.zip_longest(rem(S), rem(T)))