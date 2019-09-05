'''

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]

Output:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        result = []
        self.DFS(nums, result, 0)
        return result
    
    def DFS(self, nums, result, index):
        if index == len(nums):
            result.append(copy.deepcopy(nums))
            return
        for start in range(index, len(nums)):
            nums[start], nums[index] = nums[index], nums[start]
            self.DFS(nums, result, index + 1)
            nums[start], nums[index] = nums[index], nums[start]
        
