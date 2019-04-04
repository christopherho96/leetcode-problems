// Write a program to find the node at which the intersection of two singly linked lists begins.
// https://leetcode.com/problems/intersection-of-two-linked-lists/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        
        // Hash Table method: run time of O(m+n)
        // Space Complexity: O(m) or O(n)
        if(headA == null || headB == null) return null;
        HashSet values = new HashSet<ListNode>();
        while(headA != null){
            values.add(headA);
            headA = headA.next;
        }
        
        while(headB != null){
            if(values.contains(headB)) return headB;
            else headB = headB.next;
        }
        return headB;
        
//        Smart way to make up length differene between lists
//        Runtime: O(m+n)
//        Space Complexity O(1)
//         ListNode a = headA;
//         ListNode b = headB;
        
//         while(a != b){
//             a = a == null? headB : a.next;
//             b = b == null? headA : b.next;
//         }
        
//         return a;
    }
}