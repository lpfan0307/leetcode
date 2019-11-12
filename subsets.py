class Solution(object):
    def helper(self, sets, index,nums):
        if index == len(nums):
            return sets
        num = nums[index]
        new_sets = []
        for old_set in sets:
            new_set = [n for n in old_set]
            new_set.append(num)
            new_sets.append(new_set)
       
        sets = sets + new_sets
        return self.helper(sets, index+1,nums)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return  self.helper([[]],0,nums)
        # sets = [[]]

        # for i in range(len(nums)):
        #     new_sets = []
        #     for old_set in sets:
        #         new_set = [n for n in old_set]
        #         new_set.append(nums[i])
        #         new_sets.append(new_set)
        #     for new_set in new_sets:
        #         sets.append(new_set)
        # return sets
s = Solution()
nums = [1,2,3,4]
s.subsets(nums)

#s = [[]]
#s2 = [[1]]
#for item in s2:
#    s.append(item)
#print(s)
