// https://leetcode.com/problems/add-two-numbers/

// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = null;
        ListNode temp = null;
        int remainder = 0;
        while(l1!= null || l2 != null || remainder > 0){
            int val1 = l1 == null ? 0 : l1.val;
            int val2 = l2 == null ? 0 : l2.val;
            
            int sum = val1 + val2 + remainder;
            int digit = sum % 10;
            remainder = sum / 10;
            
            if (head == null){
                head = new ListNode(digit);
                temp = head;
            }else{
                temp.next = new ListNode(digit);
                temp = temp.next;
            }
            
            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }
        return head;
    }
}
