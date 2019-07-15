'''

103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. 

(ie, from left to right, then right to left for the next level and alternate between).

For example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = deque()
        level = 0
        queue.append(root)
        while queue:
            size = len(queue)
            curLevel = []
            for index in xrange(size):
                if level == 0:
                    cur = queue.pop()
                    curLevel.append(cur.val)
                    if cur.left:
                        queue.appendleft(cur.left)
                    if cur.right:
                        queue.appendleft(cur.right)
                else:
                    cur = queue.popleft()
                    curLevel.append(cur.val)
                    if cur.right:
                        queue.append(cur.right)
                    if cur.left:
                        queue.append(cur.left)
            level = 1 - level
            result.append(curLevel[:])
        return result
