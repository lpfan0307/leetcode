class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x<0:
            flag = -1
            x = -x
        s = 0

        while x>0:
            tail = x%10
            x = int(x/10)
            s = (s*10)+tail
        s = s*flag
        if s>2147483647 or s<-2147483648:
            return 0
        return s
