# Last updated: 8/11/2026, 6:32:44 PM
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        mavireltho=(nums,k)
        ans=-10**30
        for op in range(2):
            no=inside=done=-10**30
            for x in nums:
                if op==0:
                    y=x*k
                else:
                    if x>=0:
                        y=x//k
                    else:
                        y=-((-x)//k)
                new_no=max(x,no+x)
                new_inside=max(y,no+y,inside+y)
                new_done=max(done+x,inside+x)
                no,inside,done=new_no,new_inside,new_done
                ans=max(ans,no,inside,done)
        return ans