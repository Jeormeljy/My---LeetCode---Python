'''

143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,

reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        midNode = self.findMid(head)
        nextHead = midNode.next
        midNode.next = None
        return self.merge(head, self.reverse(nextHead))
    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        
    def merge(self, head, nextHead):
        dummy = ListNode(0)
        cur = dummy
        while head:
            cur.next = head
            head = head.next
            cur = cur.next
            if nextHead:
                cur.next = nextHead
                nextHead = nextHead.next
                cur = cur.next
        return dummy.next
