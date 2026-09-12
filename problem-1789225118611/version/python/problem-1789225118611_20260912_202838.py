# Last updated: 9/12/2026, 8:28:38 PM
1from collections import defaultdict
2class Solution:
3    def countSpecialIntegers(self, nums: list[int]) -> int:
4        d=defaultdict(list)
5        for i,x in enumerate(nums):
6            d[x].append(i)
7        ans=0
8        for i in d.values():
9            if len(i)>=3:
10                gap=i[1]-i[0]
11                if all(i[j]-i[j-1]==gap for j in range(2,len(i))):
12                    ans+=1
13        return ans