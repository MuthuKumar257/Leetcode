# Last updated: 8/11/2026, 6:48:04 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))