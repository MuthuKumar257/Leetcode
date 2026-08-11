# Last updated: 8/11/2026, 6:39:17 PM
class Solution:
    def dayOfYear(self, date: str) -> int:
        
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)