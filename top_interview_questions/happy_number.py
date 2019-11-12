class Solution(object):
    def squares_sum(self,n):
        s = 0
        while n>0:
            dealer,remainder = divmod(n,10)
            s += remainder*remainder
            n = dealer
        return s
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        s.add(n)
        while n!=1:
            v = self.squares_sum(n)
            if v in s:
                return False
            else:
                s.add(v)
                n = v
        return True
