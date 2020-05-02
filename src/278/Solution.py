# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 0, n
        while (L < R):
            mid = L + (R - L) // 2
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1
        return L
