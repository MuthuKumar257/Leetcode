// Last updated: 8/11/2026, 6:51:27 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
     ListNode t=head;
     int l=0;
     while(t!=null){
        l++;
        t=t.next;
     }
     if (l-n==0) return head.next; 
     t=head;
     if(t!=null || t.next!=null){
        for(int i=0;i<l-n-1;i++){
            t=t.next;
        }
            t.next=t.next.next;
     }
     return head;   
    }
}