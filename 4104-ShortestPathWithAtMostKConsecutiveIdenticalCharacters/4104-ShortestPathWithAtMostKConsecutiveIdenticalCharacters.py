# Last updated: 8/11/2026, 6:31:16 PM

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g=defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
        pq=[(0,0,1)]
        dist={(0,1):0}
        while pq:
            cost,u,c=heapq.heappop(pq)
            if dist.get((u,c),float('inf'))<cost:
                continue
            if u==n-1:
                return cost
            for i,j in g[u]:
                if labels[i]==labels[u]:
                    nc=c+1
                else:
                    nc=1
                if nc>k:
                    continue
                ncost=cost+j
                
                if ncost<dist.get((i,nc),float('inf')):
                    dist[(i,nc)]=ncost
                    heapq.heappush(pq,(ncost,i,nc))

        return -1