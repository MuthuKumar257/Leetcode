# Last updated: 8/11/2026, 6:33:56 PM
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        cur = sum(A)
        while A and cur <= A[-1] * 2:
            cur -= A.pop()
        return sum(A) if len(A) > 2 else -1