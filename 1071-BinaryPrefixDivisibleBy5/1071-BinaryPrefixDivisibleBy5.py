# Last updated: 8/11/2026, 6:40:34 PM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for bit in nums:
            cur = ((cur << 1) + bit) % 5
            res.append(cur == 0)
        return res
 
