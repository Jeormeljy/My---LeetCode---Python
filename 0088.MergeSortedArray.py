'''

88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.

You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:

nums1 = [1,2,3,0,0,0], m = 3

nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        end1 = m - 1
        end2 = n - 1
        while end1 >= 0 and end2 >= 0:
            if nums1[end1] >= nums2[end2]:
                nums1[index] = nums1[end1]
                end1 -= 1
            else:
                nums1[index] = nums2[end2]
                end2 -= 1
            index -= 1
        while end2 >= 0:
            nums1[index] = nums2[end2]
            end2 -= 1
            index -= 1
