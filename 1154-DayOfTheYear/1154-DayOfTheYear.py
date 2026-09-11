# Last updated: 9/11/2026, 9:38:15 AM
class Solution:
    def dayOfYear(self, date: str) -> int:
        
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)