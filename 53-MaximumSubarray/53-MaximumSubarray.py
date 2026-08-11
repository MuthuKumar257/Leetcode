# Last updated: 8/11/2026, 6:50:21 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        newNum = maxTotal = nums[0]        
        
        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)

        return maxTotal