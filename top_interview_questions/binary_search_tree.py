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
        self.left_root_right(root) #����left_root_right()����������������������������ڵ��ֵ�����б�List��
        for i in range(1,len(self.List)):
            if self.List[i]<=self.List[i-1]: #ͨ��forѭ�������б�����ǰֵ���ڻ����ǰһ��ֵ���򷵻�False
                return False
        return True 
    
    def left_root_right(self,root):
        if root==None:
            return 
        
        self.left_root_right(root.left) #���������ǰ������������
        self.List.append(root.val) #����ǰ�����ĸ��ڵ��ֵ�����б�List��
        self.left_root_right(root.right)#���������ǰ������������
