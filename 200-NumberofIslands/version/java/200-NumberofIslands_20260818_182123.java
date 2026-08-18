// Last updated: 8/18/2026, 6:21:23 PM
1public class Solution {
2
3private int n;
4private int m;
5
6public int numIslands(char[][] grid) {
7    int count = 0;
8    n = grid.length;
9    if (n == 0) return 0;
10    m = grid[0].length;
11    for (int i = 0; i < n; i++){
12        for (int j = 0; j < m; j++)
13            if (grid[i][j] == '1') {
14                DFSMarking(grid, i, j);
15                ++count;
16            }
17    }    
18    return count;
19}
20
21private void DFSMarking(char[][] grid, int i, int j) {
22    if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') return;
23    grid[i][j] = '0';
24    DFSMarking(grid, i + 1, j);
25    DFSMarking(grid, i - 1, j);
26    DFSMarking(grid, i, j + 1);
27    DFSMarking(grid, i, j - 1);
28}}