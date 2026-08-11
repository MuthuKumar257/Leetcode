# Last updated: 8/11/2026, 6:36:44 PM
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        cnt = 0
        for n in sorted(arr):
            cnt = min(cnt+1, n)
        return cnt