'''

337. House Robber III

The thief has found himself a new place for his thievery again. 

There is only one entrance to this area, called the "root." 

Besides the root, each house has one and only one parent house. 

After a tour, the smart thief realized that "all houses in this place forms a binary tree". 

It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 

Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9

Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# consider a special case that: [4, 1, null, 2, null, 3, null]
#             4
#           /   \
#         1       null
#       /   \
#     2       null
#   /
# 3
# the result is 7, so it is not guaranteed that we will pick one for two consecutive TreeNodes
# Definition: maximum amount of money without alert including root or not
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        dct = {}
        return self.helper(root, dct)
        
    def helper(self, root, dct):
        if root is None:
            return 0
        if root in dct:
            return dct[root]
        result = root.val
        if root.left:
            result += self.helper(root.left.left, dct) + self.helper(root.left.right, dct)
        if root.right:
            result += self.helper(root.right.left, dct) + self.helper(root.right.right, dct)
        result = max(result, self.helper(root.left, dct) + self.helper(root.right, dct))
        dct[root] = result
        return result
