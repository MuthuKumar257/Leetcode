# Last updated: 8/11/2026, 6:45:47 PM
class Solution:
    def addDigits(self, num: int) -> int:
        while num == 0:
            return 0
        return 1 + (num - 1) % 9