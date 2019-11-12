"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# class Solution(object):
#     def connect(self, root):
#         """
#         :type root: Node
#         :rtype: Node
#         """
#         if root is None:
#             return None
#         cur_nodes = [root]
#         while len(cur_nodes)>0:
#             new_nodes = []
#             for node in cur_nodes:
#                 if node.left is not None:
#                     new_nodes.append(node.left)
#                 if node.right is not None:
#                     new_nodes.append(node.right)
#             for i in range(len(cur_nodes)-1):
#                 cur_node = cur_nodes[i]
#                 next_node = cur_nodes[i+1]
#                 cur_node.next = next_node
#             cur_nodes = new_nodes
#         return root

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)