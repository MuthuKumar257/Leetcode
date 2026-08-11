# Last updated: 8/11/2026, 6:49:21 PM
class Solution:
    def binno(self,n:int,r:int) -> int:
        f=1
        for i in range(r):
            f*=(n-i)
            f//=(i+1)
        return f
    def numTrees(self, n: int) -> int:
        return self.binno(2*n,n)//(n+1)