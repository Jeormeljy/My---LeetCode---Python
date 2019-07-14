'''

199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, 

return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]

Output: [1, 3, 4]

Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  
'''

# Solution 1: Breadth First Search
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for index in xrange(size):
                cur = queue.popleft()
                if index == size - 1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
        
# Solution 2: Depth First Search
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if root is None:
            return
        if level == len(result):
            result.append(root.val)
        self.helper(root.right, level + 1, result)
        self.helper(root.left, level + 1, result)
