# Last updated: 9/11/2026, 9:28:52 AM
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        vis = [False] * (n + 1)
        q = deque([1])
        vis[1] = True

        ans = float('inf')

        while q:

            node = q.popleft()

            for nei, wt in adj[node]:

                ans = min(ans, wt)

                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)

        return ans