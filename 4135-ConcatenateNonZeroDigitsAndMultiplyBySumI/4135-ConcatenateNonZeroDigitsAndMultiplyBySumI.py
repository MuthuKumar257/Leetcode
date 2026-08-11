# Last updated: 8/11/2026, 6:30:54 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        m=0
        while n>0:
            t=n%10
            n=n//10
            if t==0:
                continue
            m=m*10+t
            s+=t
        return int(str(m)[::-1])*s