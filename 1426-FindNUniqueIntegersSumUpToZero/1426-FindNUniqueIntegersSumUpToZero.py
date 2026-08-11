# Last updated: 8/11/2026, 6:38:35 PM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))