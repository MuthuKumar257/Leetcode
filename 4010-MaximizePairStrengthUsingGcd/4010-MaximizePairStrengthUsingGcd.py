# Last updated: 9/11/2026, 9:20:41 AM

from math import gcd
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        result=0
        for i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                t=gcd(nums[i],nums[j])
                t1=(nums[i]*nums[j])//(t*t)
                result=max(result,t1)
        return result