class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)-1):
            j = i+1
            while j <= len(nums)-1:
                if nums[i] == nums[j]:
                    nums.remove(nums[j])
                    j -= 1
                j += 1
        return len(nums)
