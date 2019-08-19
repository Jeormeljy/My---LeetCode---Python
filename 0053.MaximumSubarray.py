'''

53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 

which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 

which is more subtle.

'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        pre = 0
        cur = 0
        result = -sys.maxint - 1
        # result = float('-inf')
        for index in xrange(len(nums)):
            cur = max(pre + nums[index], nums[index])
            pre = cur
            result = max(result, cur)
        return result
