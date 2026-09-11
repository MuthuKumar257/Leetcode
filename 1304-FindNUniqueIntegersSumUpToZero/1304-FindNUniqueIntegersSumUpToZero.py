# Last updated: 9/11/2026, 9:37:23 AM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))