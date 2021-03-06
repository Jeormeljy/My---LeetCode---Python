'''

75. Sort Colors

Given an array with n objects colored red, white or blue, 

sort them in-place so that objects of the same color are adjacent, 

with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.

First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, 

then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        zeros = 0
        ones = 0
        twos = len(nums) - 1
        while ones <= twos:
            if nums[ones] == 0:
                nums[zeros], nums[ones] = nums[ones], nums[zeros]
                ones += 1
                zeros += 1
            elif nums[ones] == 2:
                nums[ones], nums[twos] = nums[twos], nums[ones]
                twos -= 1
            else:
                ones += 1
