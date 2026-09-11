# Last updated: 9/11/2026, 9:37:31 AM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        return p-s