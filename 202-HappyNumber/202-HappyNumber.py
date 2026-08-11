# Last updated: 8/11/2026, 6:46:50 PM
class Solution(object):
    def isHappy(self, n):
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True