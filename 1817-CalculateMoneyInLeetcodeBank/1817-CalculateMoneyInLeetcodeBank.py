# Last updated: 8/11/2026, 6:37:06 PM
class Solution(object):
    def totalMoney(self, n):
        weeks, days = divmod(n, 7)
        amount = (weeks*(weeks-1)//2)*7 + weeks*28 + (days*(days+1)//2) + weeks*days
        return amount