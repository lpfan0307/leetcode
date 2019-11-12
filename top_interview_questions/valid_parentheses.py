class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        l.append(s[0])
        for i in range(1,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                l.append(s[i])
            elif not len(l):
                return False
            elif s[i]==')':
                if l[-1]=='(':
                    l.pop()
                else:
                    return False
            elif s[i]==']':
                if l[-1]=='[':
                    l.pop()
                else:
                    return False
            elif s[i]=='}':
                if l[-1]=='{':
                    l.pop()
                else:
                    return False
        if len(l):
            return False
        else:
            return True
