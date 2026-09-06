# Last updated: 9/6/2026, 8:07:23 AM
1class Solution:
2    def countGoodRotations(self, nums: list[int]) -> int:
3        n=len(nums)
4        half=n//2
5        t=sum(nums)
6        arr=nums+nums
7        ws=sum(arr[:half])
8        ans=0
9        for i in range(n):
10            if 2*ws>t:
11                ans+=1
12            ws+=arr[i+half]-arr[i]
13        return ans