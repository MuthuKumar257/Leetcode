# Last updated: 9/11/2026, 9:29:33 AM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,(2*n)+1):
            if(i%2==0 and i%n==0):
                return i