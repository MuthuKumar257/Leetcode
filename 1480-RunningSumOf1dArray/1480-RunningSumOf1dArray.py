# Last updated: 9/11/2026, 9:34:02 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        z=[]
        for i in range(1,len(nums)+1):
            z.append(sum(nums[:i]))
        return z