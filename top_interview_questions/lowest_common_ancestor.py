# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root is p or root is q:
            return root
        left_child = self.lowestCommonAncestor(root.left,p,q)
        right_child = self.lowestCommonAncestor(root.right,p,q)
        if left_child and right_child:
            return root
        if left_child:
            return left_child
        else:
            return right_child

