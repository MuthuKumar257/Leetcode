# Last updated: 8/11/2026, 6:41:18 PM
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