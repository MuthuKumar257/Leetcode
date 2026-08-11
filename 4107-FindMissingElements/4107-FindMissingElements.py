# Last updated: 8/11/2026, 6:31:12 PM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=[]
        a,b=min(nums),max(nums)
        for i in range(a,b):
            if i not in nums:
                m.append(i)
        return m