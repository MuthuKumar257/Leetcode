# Last updated: 9/3/2026, 9:05:50 AM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        d = {}
4        l = 0
5        ans = 0
6
7        for r in range(len(fruits)):
8            d[fruits[r]] = r
9
10            if len(d) > 2:
11                k = min(d, key=d.get)
12                l = d[k] + 1
13                del d[k]
14
15            ans = max(ans, r - l + 1)
16
17        return ans