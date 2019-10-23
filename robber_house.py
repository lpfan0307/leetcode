class Solution(object):
    def rob(self, nums):
        """
        :type nums : List[int]
        :rtype int
        """
        size = len(nums)
        dp = [0]*(size+1)
        if size:
            dp[1] = nums[0]
        for i in range(2,size+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[size]
