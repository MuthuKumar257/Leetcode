# Last updated: 8/11/2026, 6:46:47 PM
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        dummy = ans

        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return ans.next