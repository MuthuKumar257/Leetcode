# Last updated: 8/27/2026, 1:34:18 PM
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        res=[]
        nums=[x for x in nums if lower<=x<=upper]
        nums.sort()
        nums=[lower-1]+nums+[upper+1]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                start=nums[i-1]+1
                end=nums[i]-1
                res.append([start,end])
        return res