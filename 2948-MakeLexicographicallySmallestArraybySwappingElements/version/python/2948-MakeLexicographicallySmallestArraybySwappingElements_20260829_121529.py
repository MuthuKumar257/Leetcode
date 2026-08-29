# Last updated: 8/29/2026, 12:15:29 PM
1class Solution:
2    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
3        n = len(nums)
4
5        # Sort by value while keeping original indices
6        pairs = sorted((num, i) for i, num in enumerate(nums))
7
8        ans = nums[:]
9        start = 0
10
11        while start < n:
12            end = start
13
14            # Find all values belonging to the same group
15            while (
16                end + 1 < n
17                and pairs[end + 1][0] - pairs[end][0] <= limit
18            ):
19                end += 1
20
21            # Values are already sorted
22            values = [pairs[i][0] for i in range(start, end + 1)]
23
24            # Get and sort their original indices
25            indices = sorted(
26                pairs[i][1] for i in range(start, end + 1)
27            )
28
29            # Put smallest values at smallest indices
30            for idx, value in zip(indices, values):
31                ans[idx] = value
32
33            start = end + 1
34
35        return ans