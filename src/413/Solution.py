class Solution:
    def numberOfArithmeticSlices2(self, A: List[int]) -> int:
        def getSumFromN(n):
            if n < 3:
                return 0
            return sum(i for i in range(1, n - 1))
        if len(A) < 3:
            return 0
        prev_sum = A[1] - A[0]
        curr_count = 1
        curr_sum = 0
        for i in range(1, len(A)):
            if prev_sum == A[i] - A[i - 1]:
                curr_count += 1
            else:
                prev_sum = A[i] - A[i - 1]
                curr_sum += getSumFromN(curr_count)
                curr_count = 2
        curr_sum += getSumFromN(curr_count)
        return curr_sum

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # After refactor
        if len(A) < 3:
            return 0
        count = 0
        curr_sum = 0
        for i in range(2, len(A)):
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
                count += 1
            else:
                curr_sum += count * (count + 1) // 2
                count = 0
        curr_sum += count * (count + 1) // 2
        return curr_sum
