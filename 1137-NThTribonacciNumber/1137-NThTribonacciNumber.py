# Last updated: 9/11/2026, 9:38:38 AM
class Solution:
    def tribonacci(self, n: int) -> int:
        n1=0
        n2=1
        n3=1
        if n>0:
            for i in range(3,n+1):
                t=n1
                n1=n2
                n2=n3
                n3=t+n1+n2
            return n3
        else:
            return n