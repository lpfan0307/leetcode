class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None

        s = 0
        m = nums[0]
        for i in range(0,len(nums)):
            s+=nums[i]
            if s>m:
                m = s
            if s<0:
                s = 0
        return m
