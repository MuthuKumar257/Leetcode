# Last updated: 9/11/2026, 9:32:26 AM
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        cnt = 0
        for n in sorted(arr):
            cnt = min(cnt+1, n)
        return cnt