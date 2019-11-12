class Solution(object):
    def twoSum(self,nums,target):
        """
        :param nums:List[int]
        :param target:int
        :return:List[int
        """
        value_index_map = {}
        for i in range(len(nums)):
            value_index_map[nums[i]] = i
        for i in range(len(nums)):
            v = target-nums[i]
            if v in value_index_map:
                index = value_index_map[v]
                if i!=index:
                    return [i,index]
