# Last updated: 8/25/2026, 6:08:51 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        seen = set(nums)
4
5        cur = k
6        while cur in seen:
7            cur += k
8
9        return cur