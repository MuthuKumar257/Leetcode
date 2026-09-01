# Last updated: 9/1/2026, 10:15:08 AM
1from collections import deque
2from typing import List
3
4class Solution:
5    def minMoves(self, classroom: List[str], energy: int) -> int:
6        m, n = len(classroom), len(classroom[0])
7        litter_pos = {}
8        start = None
9        
10        for r in range(m):
11            for c in range(n):
12                if classroom[r][c] == 'S':
13                    start = (r, c)
14                elif classroom[r][c] == 'L':
15                    litter_pos[(r, c)] = len(litter_pos)
16                    
17        target_mask = (1 << len(litter_pos)) - 1
18        if target_mask == 0: 
19            return 0
20            
21        q = deque([(start[0], start[1], energy, 0, 0)])
22        visited = {(start[0], start[1], energy, 0)}
23        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
24        
25        while q:
26            r, c, e, mask, steps = q.popleft()
27            
28            for dr, dc in dirs:
29                nr, nc = r + dr, c + dc
30                
31                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
32                    nxt_e = e - 1
33                    nxt_mask = mask
34                    
35                    if classroom[nr][nc] == 'L':
36                        nxt_mask |= (1 << litter_pos[(nr, nc)])
37                        
38                    if nxt_mask == target_mask:
39                        return steps + 1
40                        
41                    if classroom[nr][nc] == 'R':
42                        nxt_e = energy
43                        
44                    if nxt_e == 0 and classroom[nr][nc] != 'R':
45                        continue
46                        
47                    if (nr, nc, nxt_e, nxt_mask) not in visited:
48                        visited.add((nr, nc, nxt_e, nxt_mask))
49                        q.append((nr, nc, nxt_e, nxt_mask, steps + 1))
50                        
51        return -1