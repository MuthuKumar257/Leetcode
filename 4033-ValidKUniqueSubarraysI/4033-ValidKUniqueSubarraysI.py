# Last updated: 9/11/2026, 9:23:03 AM
class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n=len(nums)
        q=len(queries)
        mp={}
        arr=[]
        for x in nums:
            if x not in mp:
                mp[x]=len(mp)
            
            arr.append(mp[x])
            block=int(n**0.5)
        orders=list(range(q))
        orders.sort( key=lambda i:(queries[i][0]//block,queries[i][1])  )
        freq=[0]*len(mp)
        left=0
        right=-1
        distinct=0
        odd=0
        ans=[False]*q
        def add(x):
                nonlocal distinct,odd
                if freq[x]==0:
                    distinct+=1
                if freq[x]%2==1:
                    odd-=1
                freq[x]+=1
                if freq[x]%2==1:
                    odd+=1
                    
        def remove(x):
                nonlocal distinct,odd
                if freq[x]%2==1:
                    odd-=1
                freq[x]-=1
                if freq[x]==0:
                    distinct-=1
                if freq[x]%2==1:
                    odd+=1
        for i in orders:
                l,r=queries[i]
                while right<r:
                    right+=1
                    add(arr[right])
                while right>r:
                    remove(arr[right])
                    right-=1
                while left<l:
                    remove(arr[left])
                    left+=1
                    
                while left>l:
                    left-=1
                    add(arr[left])
                ans[i]=(distinct==k and odd==0)
        return ans