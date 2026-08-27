# Last updated: 8/27/2026, 1:19:17 PM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        cnt = [0] * 26
4        for i in range(len(s)):
5            cnt[ord(s[i]) - ord("a")] += 1
6            cnt[ord(target[i]) - ord("a")] -= 1
7
8        # Try from right to left
9        t = list(target)
10        for i in range(len(s) - 1, -1, -1):
11            b = ord(t[i]) - ord("a")
12            cnt[b] += 1  # Reversal of consumption
13            # Check if the prefix can fully match
14            if min(cnt) < 0:
15                continue
16            # Find the smallest available character larger than b.
17            for j in range(b + 1, 26):
18                if cnt[j] > 0:
19                    cnt[j] -= 1
20                    t[i] = chr(ord("a") + j)
21                    return "".join(t[: i + 1]) + self.getMinString(cnt)
22
23        return ""
24
25    # Get the lexicographically smallest string (in ascending order)
26    def getMinString(self, cnt: list[int]) -> str:
27        res = []
28        for i in range(26):
29            res.append(chr(ord("a") + i) * cnt[i])
30        return "".join(res)