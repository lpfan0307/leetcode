class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        output = [[nums[0],nums[1]],[nums[1],nums[0]]]
        for i in range(2, len(nums)):
            tmp = nums[i]
            output_new = []
            for j in range(len(output)):
                output[j].append(tmp)
                output_new.append(output[j])
                for k in range(len(output[j])-1):
                    line = [n for n in output[j]]
                    line[len(line)-1] = line[k]
                    line[k] = tmp
                    output_new.append(line)
            output = output_new
        return output

