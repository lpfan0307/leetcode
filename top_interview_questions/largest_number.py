class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                temp_1 = str(nums[j])
                temp_2 = str(nums[j+1])
                if(int(temp_1+temp_2)<int(temp_2+temp_1)):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        output = ''
        for i in nums:
            output = output + str(i)
        return str(int(output))

