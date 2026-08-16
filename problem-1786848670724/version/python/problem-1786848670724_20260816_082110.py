# Last updated: 8/16/2026, 8:21:10 AM
1class Solution:
2    def maximumGap(self, skill: str, station: str) -> int:
3        n=len(skill)
4        left=[0]*n
5        right=[0]*n
6        j=0
7        for i in range(n):
8            while station[j]!=skill[i]:
9                j+=1
10            left[i]=j
11            j+=1
12        j=len(station)-1
13        for i in range(n-1,-1,-1):
14            while station[j]!=skill[i]:
15                j-=1
16            right[i]=j
17            j-=1
18        ans=0
19        for i in range(1,n):
20            ans=max(ans,right[i]-left[i-1])
21        return ans