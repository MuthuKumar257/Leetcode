# Last updated: 8/11/2026, 6:44:40 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(x) for x in s)
        t_sum = sum(ord(y) for y in t)
    
        return chr(t_sum - s_sum)