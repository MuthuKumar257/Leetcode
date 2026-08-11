# Last updated: 8/11/2026, 6:42:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            total, count = 0, 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    total += node.val
                    count += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(total / count)
        return res
                