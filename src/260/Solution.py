class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]