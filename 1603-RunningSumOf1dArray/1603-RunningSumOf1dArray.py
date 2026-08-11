# Last updated: 8/11/2026, 6:37:44 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        z=[]
        for i in range(1,len(nums)+1):
            z.append(sum(nums[:i]))
        return z