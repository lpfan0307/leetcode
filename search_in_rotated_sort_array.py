class Solution(object):
    def search(self, nums, target):
 
        l , r = 0 ,len(nums)-1 
        while l <= r :
            mid  = (l+r) //2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: 
                if target >= nums[l] and target <= nums[mid]:  
                    r = mid 
                else : 
                    l = mid +1
            if nums[mid] <= nums[r] :
                if target >= nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r= mid 
            
        return -1

