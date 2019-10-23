class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return
        left_pointer = 0
        for i in range(len(nums)):
            if nums[i]:
                temp = nums[i]
                nums[i] = nums[left_pointer]
                nums[left_pointer]=temp
                left_pointer+=1
