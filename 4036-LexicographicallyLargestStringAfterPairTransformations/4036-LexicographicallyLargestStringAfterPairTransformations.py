# Last updated: 9/11/2026, 9:21:01 AM
class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans=[]
        for n in nums:
            s=[]
            while n>0:
                p=1<<(n.bit_length()-1)
                power=min(p.bit_length()-1,25)
                s.append(chr(ord('a')+power))
                n-=(1<<power)
            ans.append("".join(s))
        return ans