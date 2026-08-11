# Last updated: 8/11/2026, 6:30:22 PM
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