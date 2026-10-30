"""
LeetCode: Shortest Path With At Most K Consecutive Identical Characters
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
"""

labels[node]
        while heap:
            d, run, x = heappop(heap)
            if run >= best[x]:  # x was settled before, no farther away and with a run no 
            longer
                continue
            if x == n - 1:
                return d
            best[x] = run
            for y, w in graph[x]:
                r = run + 1 if labels[y] == labels[x] else 1
                if r < best[y]:
                    heappush(heap, (d + w, r, y))
        return -1
