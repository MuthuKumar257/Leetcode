# Last updated: 8/29/2026, 8:32:03 PM
1class Solution:
2    def maxValidSplits(self, nums: list[int]) -> int:
3        n=len(nums)
4        ans=0
5        for remove in range(-1,n):
6            arr=[]
7            for i in range(n):
8                if i!=remove:
9                    arr.append(nums[i])
10            m=len(arr)
11            if m<2:
12                continue
13            prefix=[0]*m
14            g=0
15            for i in range(m):
16                g=gcd(g,arr[i])
17                prefix[i]=g
18            suffix=[0]*m
19            g=0
20            for i in range(m-1,-1,-1):
21                g=gcd(g,arr[i])
22                suffix[i]=g
23            score=0
24            for i in range(m-1):
25                if prefix[i]==suffix[i+1]:
26                    score+=1
27            ans=max(ans,score)
28        return ans