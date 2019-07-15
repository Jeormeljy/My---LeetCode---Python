'''

113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        cur = []
        self.DFS(root, sum, cur, result)
        return result
    def DFS(self, root, sum, cur, result):
        if root is None:
            return
        if root.left is None and root.right is None and sum == root.val:
            cur.append(root.val)
            result.append(cur[:])
            cur.pop()
            return
        cur.append(root.val)
        self.DFS(root.left, sum - root.val, cur, result)
        self.DFS(root.right, sum - root.val, cur, result)
        cur.pop()
        
