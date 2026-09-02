# Last updated: 9/2/2026, 8:00:01 PM
1class Solution:
2    def minCameraCover(self, root: TreeNode) -> int:
3        # set the value of camera nodes to 1
4        # set the value of monitored parent nodes to 2
5        def dfs(node: Optional[TreeNode]) -> int:
6            if not node:
7                return 0
8            res = dfs(node.left) + dfs(node.right)
9            # find out if current node is a root node / next node in line to be monitored
10            curr = min(
11                node.left.val if node.left else float('inf'),
12                node.right.val if node.right else float('inf'),
13            )
14            if curr == 0:
15                # at least one child node requires monitoring, this node must have a camera
16                node.val = 1
17                res += 1
18            elif curr == 1:
19                # at least one child node is a camera, this node is already monitored
20                node.val = 2
21            # if curr == float('inf'), the current node is a leaf node; let the parent node monitor this node
22            # if curr == 2, all child nodes are being monitored; treat the current node as a leaf node
23            return res
24        # ensure that root node is monitored, otherwise, add a camera onto root node
25        return dfs(root) + (root.val == 0)