# Last updated: 8/11/2026, 6:45:19 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if n==3**i:
                return True
        return False