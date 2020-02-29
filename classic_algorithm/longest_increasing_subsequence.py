class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        tail = []
        tail.append(nums[0])
        for i in range(1,len(nums)):
            #print(tail)
            target = nums[i]
            if target > tail[-1]:
                tail.append(target)
            else:
                left = 0
                right = len(tail) - 1
                while left < right:
                    mid = (left + right) // 2
                    #print(left, right,tail[mid],target )
                   
                    if target > tail[mid]:
                        left = mid + 1
                    else:
                        right = mid
                tail[right] = target
        return len(tail)

solution = Solution()
nums = [10,9,2,5,3,7,101,18]
solution.lengthOfLIS(nums)