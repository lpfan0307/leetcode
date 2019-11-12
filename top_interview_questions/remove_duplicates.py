class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        index = 0
        current_value = nums[0]
        for i in range(1,len(nums)):
            if current_value!=nums[i]:
                nums[index+1]=nums[i]
                current_value = nums[i]
                index+=1
        return index+1
