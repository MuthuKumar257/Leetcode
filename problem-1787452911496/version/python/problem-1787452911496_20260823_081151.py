# Last updated: 8/23/2026, 8:11:51 AM
1class Solution:
2    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
3        res=[]
4        nums=[x for x in nums if lower<=x<=upper]
5        nums.sort()
6        nums=[lower-1]+nums+[upper+1]
7        for i in range(1,len(nums)):
8            if nums[i]-nums[i-1]>1:
9                start=nums[i-1]+1
10                end=nums[i]-1
11                res.append([start,end])
12        return res