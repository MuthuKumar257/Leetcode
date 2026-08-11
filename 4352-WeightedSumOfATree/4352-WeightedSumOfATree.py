# Last updated: 8/11/2026, 6:30:08 PM
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent)
        c=[[] for _ in range(n)]
        for i in range(1,n):
            c[parent[i]].append(i)
        d=[0]*n
        d[0]=1
        s=[0]
        h=1
        while s:
            temp=s.pop()
            h=max(h,d[temp])
            for i in c[temp]:
                d[i]=d[temp]+1
                s.append(i)
        res=0
        for i in range(n):
            res+=nums[i]*(h-d[i]+1)
        return res