# Last updated: 8/11/2026, 6:50:42 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        a=1
    
        while a in s:
            a+=1
        return a
       