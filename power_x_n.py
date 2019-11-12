class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n >= 0:

        if n == 0:
            return 1
        if n == -1 :
            return 1/x
        ## ologn  分治二分
        return self.myPow( x * x, n // 2)  *    (  [1, x][n % 2] )
