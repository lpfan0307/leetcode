class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0]*(n+2)
        l[1] = 1
        l[2] = 2
        if n<=2:
            return l[n]
        for i in range(3,n+1):
            l[i] = l[i-1]+l[i-2]
        return l[n]
