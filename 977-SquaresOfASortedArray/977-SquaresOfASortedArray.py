# Last updated: 9/11/2026, 9:40:02 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            res.append(i**2)
        res.sort()
        return res