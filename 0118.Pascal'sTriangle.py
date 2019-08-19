'''

118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5

Output:

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        for i in xrange(numRows):
            if i == len(result):
                result.append([])
            for j in xrange(i + 1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j] + result[i - 1][j - 1])
        return result
