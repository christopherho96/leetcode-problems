# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current:
            temp = current.next
            while temp and current.val == temp.val:
                temp = temp.next
            current.next = temp
            current = temp
        return head
        