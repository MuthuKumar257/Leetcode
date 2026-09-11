# Last updated: 9/11/2026, 9:22:56 AM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a=max(nums)
        b=min(nums)
        return (a-b)*k