# Last updated: 9/11/2026, 9:31:32 AM
class Solution:
    def isThree(self, n: int) -> bool:
        a=0
        for i in range(1,n+1):
            if n%i==0:
                a+=1
        return a==3