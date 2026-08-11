# Last updated: 8/11/2026, 6:38:31 PM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next((k,n-k) for k in range(n) if '0' not in f'{k}{n-k}')