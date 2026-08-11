# Last updated: 8/11/2026, 6:46:18 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        for i in range(31):
            if n==2**i:
                return True
        return False   