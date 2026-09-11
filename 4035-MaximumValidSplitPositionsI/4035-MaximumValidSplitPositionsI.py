# Last updated: 9/11/2026, 9:20:38 AM
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for remove in range(-1,n):
            arr=[]
            for i in range(n):
                if i!=remove:
                    arr.append(nums[i])
            m=len(arr)
            if m<2:
                continue
            prefix=[0]*m
            g=0
            for i in range(m):
                g=gcd(g,arr[i])
                prefix[i]=g
            suffix=[0]*m
            g=0
            for i in range(m-1,-1,-1):
                g=gcd(g,arr[i])
                suffix[i]=g
            score=0
            for i in range(m-1):
                if prefix[i]==suffix[i+1]:
                    score+=1
            ans=max(ans,score)
        return ans