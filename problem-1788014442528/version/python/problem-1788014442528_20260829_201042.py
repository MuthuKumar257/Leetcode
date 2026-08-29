# Last updated: 8/29/2026, 8:10:42 PM
1class Solution:
2    def largestString(self, nums: list[int]) -> list[str]:
3        ans=[]
4        for n in nums:
5            s=[]
6            while n>0:
7                p=1<<(n.bit_length()-1)
8                power=min(p.bit_length()-1,25)
9                s.append(chr(ord('a')+power))
10                n-=(1<<power)
11            ans.append("".join(s))
12        return ans