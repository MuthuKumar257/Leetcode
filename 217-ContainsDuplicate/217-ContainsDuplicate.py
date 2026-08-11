# Last updated: 8/11/2026, 6:46:37 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))