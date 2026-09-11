# Last updated: 9/11/2026, 9:41:07 AM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            if i%2==0:
                r.append(i)
        for i in nums:
            if i%2!=0:
                r.append(i)
        return r