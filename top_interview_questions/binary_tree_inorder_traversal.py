class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution(object):
    def helper(self, root, l):
        if root is None:
            return 
        self.helper(root.left, l)
        l.append(root.val)
        self.helper(root.right, l)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.helper(root, l)
        return l