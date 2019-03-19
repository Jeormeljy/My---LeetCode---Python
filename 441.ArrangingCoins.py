"""

441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, 

where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:

¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:

¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right - 1:
            mid = (left + right) / 2
            if mid * (mid + 1) / 2 == n:
                return mid
            elif mid * (mid + 1) / 2 < n:
                left = mid + 1
            else:
                right = mid
        if right * (right + 1) / 2 <= n:
            return right
        elif left * (left + 1) / 2 <= n:
            return left
        return left - 1
