'''

111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
return its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = [sys.maxint]
        self.DFS(root, result, 1)
        return result[0]
    
    def DFS(self, root, result, level):
        if root is None:
            return
        if root.left is None and root.right is None:
            result[0] = min(result[0], level)
            return
        self.DFS(root.left, result, level + 1)
        self.DFS(root.right, result, level + 1)
