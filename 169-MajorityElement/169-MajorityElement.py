# Last updated: 8/11/2026, 6:47:52 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]