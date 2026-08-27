# Last updated: 8/27/2026, 1:34:53 PM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        cur = k
        while cur in seen:
            cur += k

        return cur