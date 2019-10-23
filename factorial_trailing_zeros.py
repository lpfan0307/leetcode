class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            c +=n/5
            n/=5
        return c
