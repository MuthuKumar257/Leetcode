# Last updated: 8/11/2026, 6:47:02 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        a=str(bin(n))[2:]
        return a.count('1')