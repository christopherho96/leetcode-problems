#https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        nodes = []; current = head
        while current != None:
            nodes.append(current)
            current = current.next
        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next
        prevNode = nodes[removeIndex - 1]
        prevNode.next = None if n<2 else prevNode.next.next
        return nodes[0]