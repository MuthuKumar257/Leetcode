# Last updated: 8/11/2026, 6:45:35 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=max(nums)
        for i in range(a+1):
            if i in nums:
                pass
            else:
                return i
        return a+1