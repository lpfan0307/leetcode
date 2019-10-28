class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    # def assign_root(self, root, nums):
    #     if len(nums)==0:
    #         return
    #     index = int((len(nums))/2)
    #     val = nums[index]
    #     root.val = val
    #     if len(nums) == 1:
    #         return
    #     if len(nums[:index])>0:

    #         root.left = TreeNode(0)
    #         self.assign_root(root.left, nums[:index])
    #     if len(nums[index+1:])>0:

    #         root.right = TreeNode(0)
        
    #         self.assign_root(root.right, nums[index+1:])
    def helper(self, nums):
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[int(len(nums)/2)])
        index = int((len(nums))/2)
        root.left = self.helper(nums[:index])
        root.right = self.helper(nums[index+1:])
        return root

    def sortedArrayToBST(self, nums):
        # if len(nums)==0:
        #     return None
        # root = TreeNode(nums[int(len(nums)/2)])
        # self.assign_root(root, nums)
        # return root
        if len(nums)==0:
             return None
        index = int((len(nums))/2)
        root = TreeNode(nums[int(len(nums)/2)])
        root.left = self.helper(nums[:index])
        root.right = self.helper(nums[index+1:])
        return root

print('hi')
a = [1,2,3,4,5,6]
s = Solution()
root = s.sortedArrayToBST(a)
print(root.val)