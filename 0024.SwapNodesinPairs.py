'''

24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, 

only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newHead = head.next
        head.next = self.swapPairs(head.next.next)
        newHead.next = head
        return newHead
