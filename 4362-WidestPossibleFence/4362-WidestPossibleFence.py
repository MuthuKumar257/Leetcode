# Last updated: 8/11/2026, 6:30:05 PM
from collections import Counter

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        f=Counter(planks)
        v=sorted(f.keys())
        p=Counter()
        for i,a in enumerate(v):
            for j in range(i,len(v)):
                b=v[j]
                if a==b:
                    c=f[a]//2
                else:
                    c=min(f[a],f[b])
                p[a+b]+=c
        r=0
        t=set(f)|set(p)
        for i in t:
            t=f.get(i,0)+p.get(i,0)
            r=max(r,t)


        return r