# class Solution:
#     def findKthLargest(self, nums,k):
#         heapq.heapify(nums)
#         while len(nums)>k:
#             heapq.heappop(nums)
#         return nums[0]

class Solution:
    def findKthLargest(self, nums,k):
        left = 0
        right = len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k-1:
                return nums[pos]
            if pos > k-1:
                right = pos-1
            else:
                left = pos + 1
    def partition(self, nums, left, right):
        pivot = nums[left] 
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                t = nums[l]
                nums[l] = nums[r]
                nums[r] = t
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        
        t = nums[left]
        nums[left] = nums[r]
        nums[r] = t

        return r
s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
s.findKthLargest(nums,4)