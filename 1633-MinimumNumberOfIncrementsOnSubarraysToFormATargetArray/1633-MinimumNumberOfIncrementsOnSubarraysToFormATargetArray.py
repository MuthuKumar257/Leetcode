# Last updated: 8/11/2026, 6:37:33 PM
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res