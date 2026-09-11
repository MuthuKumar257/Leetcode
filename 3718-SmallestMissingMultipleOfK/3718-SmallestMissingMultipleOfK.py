# Last updated: 9/11/2026, 9:22:31 AM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        cur = k
        while cur in seen:
            cur += k

        return cur