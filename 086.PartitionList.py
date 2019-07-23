'''

86. Partition List

Given a linked list and a value x, 

partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3

Output: 1->2->2->4->3->5

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummySmall = ListNode(0)
        dummyLarge = ListNode(0)
        curSmall = dummySmall
        curLarge = dummyLarge
        while head:
            if head.val < x:
                curSmall.next = head
                curSmall = curSmall.next
            else:
                curLarge.next = head
                curLarge = curLarge.next
            head = head.next
        curSmall.next = dummyLarge.next
        curLarge.next = None
        return dummySmall.next
