'''

250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = [0]
        self.helper(root, result)
        return result[0]
    
    def helper(self, root, result):
        if root is None:
            return True
        left = self.helper(root.left, result)
        right = self.helper(root.right, result)
        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            result[0] += 1
            return True
        return False
