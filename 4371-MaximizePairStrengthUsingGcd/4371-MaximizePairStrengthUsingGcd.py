# Last updated: 8/11/2026, 6:29:56 PM

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