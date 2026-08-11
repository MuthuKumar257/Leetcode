# Last updated: 8/11/2026, 6:30:23 PM
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        a1=0
        for i in range(len(nums)):
            e,o=0,0
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    e+=1
                else:
                    o+=1
                if o>0 and e*b<=o*a:
                    a1+=1
        return a1