"""

234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2

Output: false

Example 2:

Input: 1->2->2->1

Output: true

Follow up:

Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            list.append(head.val)
            head = head.next
        left = 0
        right = len(list) - 1
        while left < right:
            if list[left] != list[right]:
                return False
            left = left + 1
            right = right - 1
        return True
