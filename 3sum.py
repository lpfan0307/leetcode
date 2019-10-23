class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s<0:
                    j+=1
                elif s>0:
                    k-=1
                else:
                    l = []
                    l.append(nums[i])
                    l.append(nums[j])
                    l.append(nums[k])
                    result.append(l)
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    k-=1
                    while nums[k]==nums[k+1] and j<k:
                        k-=1
        return result
