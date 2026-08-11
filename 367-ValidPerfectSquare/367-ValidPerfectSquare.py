# Last updated: 8/11/2026, 6:44:53 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(sqrt(num))**2==num
        