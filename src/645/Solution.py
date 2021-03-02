class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicated_num = None
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicated_num = abs(nums[i])
            else:
                nums[index] = -nums[index]
        non_duplicated_num = None
        for i,n in enumerate(nums):
            if n > 0:
                non_duplicated_num = i + 1
                break
        return [duplicated_num, non_duplicated_num]
        
        