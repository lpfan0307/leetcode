class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])]<0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]

nums = [2,2,2,2]
s = Solution()
s.findDuplicate(nums)
print(nums)