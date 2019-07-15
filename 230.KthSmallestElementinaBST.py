'''

230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1

   3
  / \
 1   4
  \
   2

Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3

       5
      / \
     3   6
    / \
   2   4
  /
 1

Output: 3

Follow up:

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 

How would you optimize the kthSmallest routine?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return 0
        index = [0]
        result = [sys.maxint]
        self.helper(root, k, index, result)
        return result[0]
    def helper(self, root, k, index, result):
        if root is None or index[0] > k:
            return
        self.helper(root.left, k, index, result)
        index[0] += 1
        if index[0] == k:
            result[0] = root.val
        self.helper(root.right, k, index, result)
        
