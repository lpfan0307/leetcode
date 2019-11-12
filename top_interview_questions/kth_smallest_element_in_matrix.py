class Solution(object):
    def kthSmallest(self, matrix, k):

        def binary_count(nums, target): # count how many element LE target
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r + 1) / 2
                if nums[mid] < target + 1:
                    l = mid
                else:
                    r = mid - 1
            return l + 1 if nums[l] <= target else l
                
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if sum(binary_count(row, mid) for row in matrix) >= k:
                r = mid
            else:
                l = mid + 1
        return l