# Last updated: 8/11/2026, 6:40:54 PM
class Solution:
    def fib(self, n: int) -> int:
        n1,n2=-1,1
        for i in range(n+1):
            t=n1
            n1=n2
            n2=t+n2
        return n2