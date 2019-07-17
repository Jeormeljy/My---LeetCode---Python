'''

538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree 

such that every key of the original BST is changed to the original key plus sum of all keys greater 

than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:

              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             
             18
            /   \
          20     13

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        curSum = [0]
        self.reversedInOrder(root, curSum)
        return root
    def reversedInOrder(self, root, curSum):
        if root is None:
            return
        self.reversedInOrder(root.right, curSum)
        root.val += curSum[0]
        curSum[0] = root.val
        self.reversedInOrder(root.left, curSum)
