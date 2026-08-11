# Last updated: 8/11/2026, 6:34:49 PM
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                s+=i
        return s