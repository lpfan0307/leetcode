class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        res.append(1)
        temp = 1
        for i in range(len(nums)-1):
            temp *= nums[i]
            res.append(temp)
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp = temp * nums[i+1]
            res[i] = res[i] * temp
        return res
