# Last updated: 8/11/2026, 6:45:10 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            if n==4**i:
                return True
        return False