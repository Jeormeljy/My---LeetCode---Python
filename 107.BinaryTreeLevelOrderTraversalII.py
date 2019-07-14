'''

107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. 

(ie, from left to right, level by level from leaf to root).

For example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''

# Solution 1: Breadth First Search: same as Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            size = len(queue)
            curLevel = []
            for times in xrange(size):
                cur = queue.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.insert(0, curLevel[:])
        return result
        
# Solution 2: Depth First Search
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.helper(root, result, 0)
        return result
    def helper(self, root, result, level):
        if root is None:
            return
        if level >= len(result):
            result.insert(0, [])
        self.helper(root.left, result, level + 1)
        self.helper(root.right, result, level + 1)
        result[len(result) - level - 1].append(root.val)
