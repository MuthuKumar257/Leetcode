# Last updated: 8/11/2026, 6:35:18 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(2,(2*n)+1):
            if(i%2==0 and i%n==0):
                return i