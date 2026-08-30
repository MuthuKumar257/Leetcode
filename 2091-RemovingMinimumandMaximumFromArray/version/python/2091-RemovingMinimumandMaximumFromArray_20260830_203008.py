# Last updated: 8/30/2026, 8:30:08 PM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3        minp, maxp, minel, maxel, L = 0, 0, float('inf'), float('-inf'), len(nums)
4        for i, n in enumerate(nums):
5            if n > maxel:
6                maxel = n
7                maxp = i
8            if n < minel:
9                minel = n
10                minp = i
11        
12        left, right = min(minp, maxp), max(minp, maxp)
13
14        return min(right + 1, L - left, left + 1 + (L - right))