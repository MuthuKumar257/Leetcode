# Last updated: 8/11/2026, 6:48:37 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=nums[0]
        for i in range(1,len(nums)):
            s=s^nums[i]
        return s