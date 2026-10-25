/*
 * LeetCode: Reverse Linked List
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/reverse-linked-list/
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode a=head;
        ListNode ab=null;
        while(a!=null){
            ListNode t=a.next;
            a.next=ab;
            ab=a;
            a =t;
        }
        return ab;
    }
}
