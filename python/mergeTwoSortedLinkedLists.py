#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        current = ListNode(0)
        head = current
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
        
        l3 = l1 if l1 else l2
        current.next = l3
            
        return head.next