# Last updated: 9/11/2026, 9:37:20 AM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next((k,n-k) for k in range(n) if '0' not in f'{k}{n-k}')