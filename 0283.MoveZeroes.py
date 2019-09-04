'''

283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it

while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]

Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.

Minimize the total number of operations.

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        slow = -1
        fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
