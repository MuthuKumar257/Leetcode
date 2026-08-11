# Last updated: 8/11/2026, 6:32:13 PM
class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        def dfs(u, p):
            up[u][0] = p
            for i in range(1, bits):
                up[u][i] = up[up[u][i-1]][i-1]
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            for i in range(bits):
                if d >> i & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in reversed(range(bits)):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        n = len(edges) + 1
        g = [[] for _ in range(n+1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        bits = (n).bit_length()
        up = [[0]*(bits) for _ in range(n+1)]
        depth = [0]*(n+1)
        dfs(1, 0)
        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            l = lca(u, v)
            dist = depth[u] + depth[v] - 2*depth[l]
            if dist == 0:
                res.append(0)
                continue
            res.append(pow(2, dist-1, 10**9 + 7) % (10**9 + 7))
        return res