# Last updated: 8/12/2026, 9:38:12 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def swapPairs(self, head):
9        dummy = ListNode(-1)
10        dummy.next = head
11        ptr1 = dummy
12        ptr2 = head
13        if not head or not head.next:
14            return head
15        ptr3 = head.next
16        while ptr2 and ptr3:
17            ptr2.next = ptr3.next
18            ptr3.next = ptr2
19            ptr1.next = ptr3
20            if ptr2.next:
21                ptr3 = ptr2.next.next
22            else:
23                break
24            ptr1 = ptr2
25            ptr2 = ptr2.next
26        return dummy.next