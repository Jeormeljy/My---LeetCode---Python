'''

19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''

# Solution 1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listLength = self.getLength(head)
        dummy = ListNode(0)
        cur = dummy
        for num in xrange(listLength - n):
            cur.next = head
            head = head.next
            cur = cur.next
        cur.next = head.next
        return dummy.next
        
    def getLength(self, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result
        
# Solution 2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        advance = dummy
        for step in xrange(n + 1):
            advance = advance.next
        while advance:
            cur = cur.next
            advance = advance.next
        cur.next = cur.next.next
        return dummy.next
