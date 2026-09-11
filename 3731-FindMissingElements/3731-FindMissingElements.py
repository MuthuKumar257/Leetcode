# Last updated: 9/11/2026, 9:22:23 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=[]
        a,b=min(nums),max(nums)
        for i in range(a,b):
            if i not in nums:
                m.append(i)
        return m