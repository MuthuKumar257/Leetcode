# Last updated: 8/23/2026, 8:35:49 AM
1class Solution:
2    def longestSubarray(self, nums: list[int], k: int) -> int:
3        def factor(n):
4            s=set()
5            d=2
6            while d*d<=n:
7                if n%d==0:
8                    s.add(d)
9                    while n%d==0:
10                        n//=d
11                d+=1
12            if n>1:
13                s.add(n)
14            return s
15        pf=[factor(x) for x in nums]
16        l=0
17        c={}
18        ans=0
19        for r in range(len(nums)):
20            for p in pf[r]:
21                c[p]=c.get(p,0)+1
22            while len(c)>k:
23                for p in pf[l]:
24                    c[p]-=1
25                    if c[p]==0:
26                        del c[p]
27                l+=1
28            ans=max(ans,r-l+1)
29        return ans