class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total_num = 1
        for i in range(1,len(nums)+1):
            total_num*=i
        result = []
        while total_num>0:
            l = [i for i in nums]
            result.append(l)
            # print(nums)
            total_num-=1
            self.nextPermutation(nums)
        # print(result)
        return result
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)
        # find pivot
        pivot = right - 1
        successor = 0
        # find rightmost succesor
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)


    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
