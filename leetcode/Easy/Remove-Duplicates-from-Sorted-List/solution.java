/*
 * LeetCode: Remove Duplicates from Sorted List
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
 */

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode t=head;
        while(t!=null && t.next!=null){
            if(t.val==t.next.val){
            t.next=t.next.next;
            }else{
            t=t.next;
            }
        }
        return head;
    }
}
