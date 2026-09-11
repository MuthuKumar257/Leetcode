/*
 * LeetCode: Intersection of Two Linked Lists
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
 */

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode lista = headA;
        ListNode listb = headB;

        while (lista != listb) {
            lista = (lista != null) ? lista.next : headB;
            listb = (listb != null) ? listb.next : headA;
        }

        return lista;        
    }
}
