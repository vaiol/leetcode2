class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segmentTree = [0] * (len(nums) * 4)
        self.initSegmentTree(nums, 0, 0, len(nums) - 1)
    
    def initSegmentTree(self, arr: List[int], treeIndex: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.segmentTree[treeIndex] = arr[lo]
            return
        
        mid = lo + (hi - lo) // 2
        self.initSegmentTree(arr, treeIndex * 2 + 1, lo, mid)
        self.initSegmentTree(arr, treeIndex * 2 + 2, mid + 1, hi)
        
        self.segmentTree[treeIndex] = self.segmentTree[treeIndex * 2 + 1] + self.segmentTree[treeIndex * 2 + 2]
    
    def updateSegmentTree(self, index: int, val: int, treeIndex: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.segmentTree[treeIndex] = val
            return
        
        mid = lo + (hi - lo) // 2
        if index <= mid:
            self.updateSegmentTree(index, val, treeIndex * 2 + 1, lo, mid)
        else:
            self.updateSegmentTree(index, val, treeIndex * 2 + 2, mid + 1, hi)
        
        self.segmentTree[treeIndex] = self.segmentTree[treeIndex * 2 + 1] + self.segmentTree[treeIndex * 2 + 2]
        
    def querySegmentTree(self, left: int, right: int, treeIndex: int, lo: int, hi: int) -> int:
        if left > hi or right < lo:
            return 0
        
        if left <= lo and right >= hi:
            return self.segmentTree[treeIndex]
        
        mid = lo + (hi - lo) // 2
        if right <= mid:
            return self.querySegmentTree(left, right, treeIndex * 2 + 1, lo, mid)
        elif left > mid:
            return self.querySegmentTree(left, right, treeIndex * 2 + 2, mid + 1, hi)
        
        return self.querySegmentTree(left, right, treeIndex * 2 + 1, lo, mid) + self.querySegmentTree(left, right, treeIndex * 2 + 2, mid + 1, hi)
        

    def update(self, index: int, val: int) -> None:
        self.updateSegmentTree(index, val, 0, 0, len(self.nums) - 1)
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return self.querySegmentTree(left, right, 0, 0, len(self.nums) - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)