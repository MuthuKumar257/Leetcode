# Last updated: 8/28/2026, 9:32:58 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3
4        row = len(matrix)
5        col = len(matrix[0])
6
7        start = 0
8        end = row * col - 1
9
10        while start <= end:
11
12            mid = start + (end - start) // 2
13
14            r = mid // col
15            c = mid % col
16
17            val = matrix[r][c]
18
19            if val == target:
20                return True
21
22            elif val < target:
23                start = mid + 1
24
25            else:
26                end = mid - 1
27
28        return False