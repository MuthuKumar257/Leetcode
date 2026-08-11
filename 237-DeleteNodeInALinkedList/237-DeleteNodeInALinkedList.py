# Last updated: 8/11/2026, 6:46:07 PM
class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        if not node or not node.next:
            return  # Edge case: last node can't be deleted this way

        node.val = node.next.val  # Copy next node's value
        node.next = node.next.next  # Skip the next node, effectively deleting it