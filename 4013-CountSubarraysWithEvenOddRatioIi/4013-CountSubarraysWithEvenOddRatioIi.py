# Last updated: 9/11/2026, 9:21:24 AM
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        p=[0]
        s=0
        for i in nums:
            s+=b if i%2==0 else -a
            p.append(s)
        a1=0
        q=[]
        for i in p:
            t=bisect_left(q,i)
            a1+=len(q)-t
            insort(q,i)
        return a1