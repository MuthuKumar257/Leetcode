# Last updated: 8/11/2026, 6:31:34 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a=max(nums)
        b=min(nums)
        return (a-b)*k