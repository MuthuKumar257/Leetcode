# Last updated: 8/11/2026, 6:30:18 PM
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        r=0
        for i in range(k):
            if mul>0:
                r+=nums[i]*mul
            else:
                r+=nums[i]
            mul-=1
        return r