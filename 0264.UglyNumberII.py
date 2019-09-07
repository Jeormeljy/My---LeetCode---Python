'''

264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10

Output: 12

Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

1 is typically treated as an ugly number.

n does not exceed 1690.

'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [1] * n
        index2, index3, index5 = 0, 0, 0
        for index in range(1, n):
            lst[index] = min(lst[index2] * 2, lst[index3] * 3, lst[index5] * 5)
            if lst[index] == lst[index2] * 2:
                index2 += 1
            if lst[index] == lst[index3] * 3:
                index3 += 1
            if lst[index] == lst[index5] * 5:
                index5 += 1
        return lst[n - 1]
