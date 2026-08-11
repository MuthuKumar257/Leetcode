// Last updated: 8/11/2026, 6:46:39 PM
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