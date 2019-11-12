class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        if nums==[]:
            return 0
        dp = [1]*len(nums)
        for i in range(len(nums)-1):
            for j in range(0, i+1):
                if nums[i+1] > nums[j]:
                    dp[i+1] = max(1+dp[j],dp[i+1])
        return max(dp)