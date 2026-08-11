# Last updated: 8/11/2026, 6:38:45 PM
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flat,m,n = list(chain.from_iterable(grid)), len(grid), len(grid[0])
        return  [(flat[-(k % (m*n)):]+flat)[i*n : (i+1)*n] for i in range(m)]
        