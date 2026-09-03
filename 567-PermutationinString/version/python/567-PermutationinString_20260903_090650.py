# Last updated: 9/3/2026, 9:06:50 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
9        mp = defaultdict(lambda: [])
10        
11        def traverse(node, x, y):
12            if not node:
13                return
14            mp[x].append((y, node.val))
15            traverse(node.left, x-1, y+1)
16            traverse(node.right, x+1, y+1)
17        
18        traverse(root, 0, 0)
19        
20        result = []
21        for x in sorted(mp.keys()):
22            mp[x].sort()
23            result.append([val for _, val in mp[x]])
24        
25        return result