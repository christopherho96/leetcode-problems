#https://leetcode.com/problems/add-two-numbers/submissions/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = None; current = None; carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1 = l1 if l1 != None else ListNode(0)
            l2 = l2 if l2 != None else ListNode(0)
            sum = l1.val + l2.val + carry
            if head == None:
                head = ListNode(sum % 10)
                current = head
            else:
                current.next = ListNode(sum % 10)
                current = current.next
            carry = sum / 10
            l1 = l1.next; l2 = l2.next
        return head