# Last updated: 8/16/2026, 8:37:35 AM
1class Solution:
2
3    def stoneGameIX(self, stones: List[int]) -> bool:
4        cnt = [0] * 3
5        for stone in stones:
6            cnt[stone % 3] += 1
7
8        if cnt[0] % 2 == 0:
9            return cnt[1] >= 1 and cnt[2] >= 1
10        else:
11            return abs(cnt[1] - cnt[2]) > 2