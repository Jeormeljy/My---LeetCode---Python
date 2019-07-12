'''

96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3

Output: 5

Explanation:

Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(1)
        for i in xrange(1, n + 1):
            temp = 0
            for j in xrange(1, i + 1):
                temp += dp[j - 1] * dp[i - j]
            dp.append(temp)
        return dp[n]
