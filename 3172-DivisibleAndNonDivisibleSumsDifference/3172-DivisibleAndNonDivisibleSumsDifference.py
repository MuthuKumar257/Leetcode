# Last updated: 8/11/2026, 6:34:16 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d=[]
        nd=[]
        for i in range(1,n+1):
            if i%m==0:
                d.append(i)
            else:
                nd.append(i)
        return sum(nd)-sum(d)