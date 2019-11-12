class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx1 = 0
        l = []
        s = s.lower()
        for i, item in enumerate(s):
            if item >='a' and item <='z':
                l.append(item)
            if item>='0' and item<='9':
                l.append(item)
        for i in range(int(len(l)/2)):
            j = len(l)-i-1
            if l[i] != l[j]:
                return False
        return True