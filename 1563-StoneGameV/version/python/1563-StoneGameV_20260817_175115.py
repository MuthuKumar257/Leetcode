# Last updated: 8/17/2026, 5:51:15 PM
1class Solution:
2    def stoneGameV(self, stoneValue: List[int]) -> int:
3        prefix = list(accumulate(stoneValue, initial=0))
4
5        @cache
6        def dfs(l, r):
7            if l >= r:
8                return 0
9
10            ans = 0
11            left_sum = 0
12            right_sum = prefix[r + 1] - prefix[l]
13
14            for k in range(l, r):
15                left_sum += stoneValue[k]
16                right_sum -= stoneValue[k]
17
18                if left_sum < right_sum:
19                    # Alice keeps the left side.
20                    #
21                    # If ans >= 2 * left_sum, this split
22                    # cannot improve the answer.
23                    if ans >= 2 * left_sum:
24                        continue
25
26                    ans = max(
27                        ans,
28                        left_sum + dfs(l, k)
29                    )
30
31                elif left_sum > right_sum:
32                    # Alice keeps the right side.
33                    #
34                    # As k increases, right_sum decreases.
35                    # If ans >= 2 * right_sum, then every
36                    # later split is also useless.
37                    if ans >= 2 * right_sum:
38                        break
39
40                    ans = max(
41                        ans,
42                        right_sum + dfs(k + 1, r)
43                    )
44
45                else:
46                    # Equal sums: Alice can choose either side.
47                    ans = max(
48                        ans,
49                        left_sum + dfs(l, k),
50                        right_sum + dfs(k + 1, r)
51                    )
52
53            return ans
54
55        return dfs(0, len(stoneValue) - 1)