class Solution(object):
    def get_dic(self,s):
        d = {}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        return d
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size = len(s)
        if size != len(t):
            return False
        d1 = self.get_dic(s)
        d2 = self.get_dic(t)
        for key in d1:
            if key not in d2:
                return False
            if d1[key] != d2[key]:
                return  False
        return True
