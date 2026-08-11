# Last updated: 8/11/2026, 6:30:35 PM
class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD=10**9+7
        def count(x):
            c=0
            for v,d in zip(value,decay):
                if v<x:
                    continue
                c+=(v-x)//d+1
            return c
        l,r=1,max(value)
        while l<=r:
            mid=(l+r)//2
            if count(mid)>=m:
                l=mid+1
            else:
                r=mid-1
        T=r
        res=0
        cmp=0
        for i,j in zip(value,decay):
            if i<T+1:
                continue
            k=(i-(T+1))//j+1
            cmp+=k
            last=i-(k-1)*j
            res+=k*(i+last)//2
        res+=(m-cmp)*T
        return res%MOD