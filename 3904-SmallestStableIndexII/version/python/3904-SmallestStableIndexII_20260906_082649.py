# Last updated: 9/6/2026, 8:26:49 AM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        mini = [0] * n
5
6        mint = float('inf')
7        for i in range(n - 1, -1, -1):
8            if nums[i] < mint:
9                mint = nums[i]
10            mini[i] = mint
11
12        maxt = 0
13        for i in range(n):
14            if nums[i] > maxt:
15                maxt = nums[i]
16            if maxt - mini[i] <= k:
17                return i
18
19        return -1