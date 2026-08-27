# Last updated: 8/27/2026, 1:34:31 PM
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def factor(n):
            s=set()
            d=2
            while d*d<=n:
                if n%d==0:
                    s.add(d)
                    while n%d==0:
                        n//=d
                d+=1
            if n>1:
                s.add(n)
            return s
        pf=[factor(x) for x in nums]
        l=0
        c={}
        ans=0
        for r in range(len(nums)):
            for p in pf[r]:
                c[p]=c.get(p,0)+1
            while len(c)>k:
                for p in pf[l]:
                    c[p]-=1
                    if c[p]==0:
                        del c[p]
                l+=1
            ans=max(ans,r-l+1)
        return ans