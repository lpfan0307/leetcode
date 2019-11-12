class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left==None and root.right==None:
            return True 
            
        self.List=[]
        self.left_root_right(root) #调用left_root_right()函数，中序遍历二叉搜索树，将节点的值存入列表List中
        for i in range(1,len(self.List)):
            if self.List[i]<=self.List[i-1]: #通过for循环遍历列表，若当前值少于或等于前一个值，则返回False
                return False
        return True 
    
    def left_root_right(self,root):
        if root==None:
            return 
        
        self.left_root_right(root.left) #中序遍历当前子树的左子树
        self.List.append(root.val) #将当前子树的根节点的值存入列表List中
        self.left_root_right(root.right)#中序遍历当前子树的右子树
