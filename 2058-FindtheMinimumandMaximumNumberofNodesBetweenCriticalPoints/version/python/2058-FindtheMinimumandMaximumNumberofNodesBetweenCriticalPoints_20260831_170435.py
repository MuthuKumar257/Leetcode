# Last updated: 8/31/2026, 5:04:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        i, sz, p0, p, minD= 1, 0, -1, -1, 2**31
9        x0, x1= head.val, head.next.val
10        less, bigger= x1<x0, x1>x0
11        Next=head.next.next
12        while Next:
13            x=Next.val
14            bigger1, less1=x>x1, x<x1
15            if (less and bigger1) or (bigger and less1):
16                if sz==0: p0=i
17                sz+=1
18                if p!=-1: minD=min(minD, i-p)
19                p=i
20            bigger, less=bigger1, less1
21            x1=x
22            i+=1
23            Next=Next.next
24        if sz<=1: return [-1,-1]
25        else: return [minD, p-p0]
26        
27        