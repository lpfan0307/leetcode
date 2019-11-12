# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder_traverse(self, root, k):
        if not root or self.flag:
            return
        self.inorder_traverse(root.left, k)
        self.cn += 1
        if self.cn == k:
            self.res = root.val
            self.flag = True
        self.inorder_traverse(root.right, k)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cn=0
        self.flag=False
        self.res=None
        self.inorder_traverse(root,k)
        return self.res
        