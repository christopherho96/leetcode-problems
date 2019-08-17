# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        current = head; newHead = None; prev = None
        while current != None and current.next != None:
            # move in pairs
            left = current
            right = current.next
            
            # swap the pairs left and right
            left.next = right.next
            right.next = left
            
            # assign the newhead if we just started from beginning
            if not newHead:
                newHead = right
                
            # point the previous node to the new left of the swapped pair
            if prev != None:
                prev.next = right
            
            # move on to the next pair
            prev = left
            current = left.next  
            
        return head if newHead is None else newHead