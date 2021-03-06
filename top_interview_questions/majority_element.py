class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate_num = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count==0:
                candidate_num = nums[i]
                count+=1
                continue
            if candidate_num!=nums[i]:
                count -=1
            else:
                count+=1
        return candidate_num
