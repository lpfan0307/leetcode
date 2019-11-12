class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        l = []
        self.traverse(root, l, 0)
        return l
    def traverse(self, root, l, depth):
        if root is  None:
            return
        if len(l) < depth + 1:
            l.append([])
        l[depth].append(root.val)
        self.traverse(root.left, l, depth+1)
        self.traverse(root.right, l, depth+1)
