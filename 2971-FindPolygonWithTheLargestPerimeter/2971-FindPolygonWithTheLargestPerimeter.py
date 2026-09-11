# Last updated: 9/11/2026, 9:26:04 AM
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        cur = sum(A)
        while A and cur <= A[-1] * 2:
            cur -= A.pop()
        return sum(A) if len(A) > 2 else -1