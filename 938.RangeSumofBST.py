'''

938. Range Sum of BST

Given the root node of a binary search tree, 

return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15

Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10

Output: 23
 
Note:

The number of nodes in the tree is at most 10000.

The final answer is guaranteed to be less than 2^31.

'''

# Solution 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None or L > R:
            return 0
        curSum = [0]
        self.inOrder(root, L, R, curSum)
        return curSum[0]
    def inOrder(self, root, L, R, curSum):
        if root is None:
            return
        self.inOrder(root.left, L, R, curSum)
        if root.val >= L and root.val <= R:
            curSum[0] += root.val
        self.inOrder(root.right, L, R, curSum)

# Solution 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None or L > R:
            return 0
        result = 0
        if root.val > L:
            result += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            result += self.rangeSumBST(root.right, L, R)
        if root.val >= L and root.val <= R:
            result += root.val
        return result
