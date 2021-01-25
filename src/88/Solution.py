class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        N = m + n - 1
        i2 = n - 1
        i1 = m - 1
        if N == 0:
            nums1[0] = nums1[0] if m > n else nums2[0]
        for i in range(N, -1, -1):
            if i1 == -1 or (i2 != -1 and nums2[i2] > nums1[i1]):
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
        