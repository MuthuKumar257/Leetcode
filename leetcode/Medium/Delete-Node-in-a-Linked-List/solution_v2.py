"""
LeetCode: Delete Node in a Linked List
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        if not node or not node.next:
            return  # Edge case: last node can't be deleted this way

        node.val = node.next.val  # Copy next node's value
        node.next = node.next.next  # Skip the next node, effectively deleting it
