# Last updated: 9/11/2026, 9:39:37 AM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for bit in nums:
            cur = ((cur << 1) + bit) % 5
            res.append(cur == 0)
        return res
 
