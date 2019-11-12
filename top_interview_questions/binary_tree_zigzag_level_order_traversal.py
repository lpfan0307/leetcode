# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if root is None:
#             return []
#         l = []
#         cur_nodes = [root]
#         flag = 0
#         while len(cur_nodes)!=0:
#             nums = []
#             new_nodes = []
#             for node in cur_nodes:
#                 nums.append(node.val)
#                 if node.left is not None:
#                     new_nodes.append(node.left)
#                 if node.right is not None:
#                     new_nodes.append(node.right)
#             cur_nodes = new_nodes
#             if flag%2==1:
#                 l.append(nums[::-1])
#             else:
#                 l.append(nums)
#             flag += 1
#         return l

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0: res[level].append(root.val)
            else: res[level].insert(0, root.val) # Ïò0Î»ÖÃ²åÈë
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def zigzagLevelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res
