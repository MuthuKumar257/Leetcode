# Last updated: 8/23/2026, 11:09:00 PM
1class Solution:
2    def sumGame(self, num: str) -> bool:
3        n = len(num)
4        sumL = sumR = qL = qR = 0
5
6        for i in range(n):
7            if i < n // 2:
8                if num[i] == '?':
9                    qL += 1
10                else:
11                    sumL += int(num[i])
12            else:
13                if num[i] == '?':
14                    qR += 1
15                else:
16                    sumR += int(num[i])
17
18        # Case 1: string only contains digits
19        if qL + qR == 0:
20            return sumL != sumR
21
22        # Case 2: odd no. of '?'
23        if (qL + qR) % 2:
24            return True
25
26        # Case 3: even no. of '?'
27        # 3a:
28        if qL == qR:
29            return sumL != sumR
30
31        # 3b: 
32        return 2 * (sumL - sumR) != 9 * (qR - qL)