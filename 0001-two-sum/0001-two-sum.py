class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solutions = [(n, i) for n in range(len(nums)) for i in range(n+1, len(nums)) if nums[n] + nums[i] == target and n != i]
        return(solutions[0])