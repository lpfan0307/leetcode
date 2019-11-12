class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)+1)//2
        left, right = nums[:mid], nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
