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

# Solution 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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
        result = [0]
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

# Solution 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        leftCount = self.getCount(root.left)
        if leftCount == k - 1:
            return root.val
        elif leftCount < k - 1:
            return self.kthSmallest(root.right, k - leftCount - 1)
        else:
            return self.kthSmallest(root.left, k)
        
        
    def getCount(self, root):
        if root is None:
            return 0
        return self.getCount(root.left) + self.getCount(root.right) + 1
   
# Solution 3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        self.pushLeft(root, stack)
        while k > 1:
            cur = stack.pop()
            k -= 1
            if cur.right:
                self.pushLeft(cur.right, stack)
        return stack.pop().val
        
    def pushLeft(self, root, stack):
        while root:
            stack.append(root)
            root = root.left
