'''

105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:

You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]

inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inDic = self.getDict(inorder)
        return self.helper(preorder, 0, len(preorder) - 1, inDic, 0, len(inorder) - 1)
    def helper(self, preorder, pstart, pend, inDic, instart, inend):
        if instart > inend:
            return None
        rootValue = preorder[pstart]
        rootIndex = inDic[rootValue]
        root = TreeNode(rootValue)
        root.left = self.helper(preorder, pstart + 1, pstart + rootIndex - instart, inDic, instart, rootIndex - 1)
        root.right = self.helper(preorder, pend - (inend - rootIndex) + 1, pend, inDic, rootIndex + 1, inend)
        return root
    def getDict(self, inorder):
        dic = {}
        for index in xrange(len(inorder)):
            dic[inorder[index]] = index
        return dic
