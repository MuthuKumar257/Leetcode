# Last updated: 9/3/2026, 9:04:45 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1, n2 = len(s1), len(s2)
4        if n2 < n1:
5            return False
6
7        c1 = [0] * 26
8        c2 = [0] * 26
9
10        for i in range(n1):
11            c1[ord(s1[i]) - ord('a')] += 1
12            c2[ord(s2[i]) - ord('a')] += 1
13
14        if c1 == c2:
15            return True
16
17        for i in range(n1, n2):
18            c2[ord(s2[i]) - ord('a')] += 1
19            c2[ord(s2[i - n1]) - ord('a')] -= 1
20
21            if c1 == c2:
22                return True
23
24        return False