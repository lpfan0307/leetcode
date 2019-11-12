class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ispositive = True
        if dividend > 0 and divisor < 0:
            ispositive = False
        if dividend < 0 and divisor > 0:
            ispositive = False
        dividend = abs(dividend);divisor = abs(divisor)
        if dividend < divisor:
            return 0
        tmp = divisor
        ans = 1
        while dividend >= tmp:
            tmp <<= 1
            if tmp > dividend:
                break
            ans <<= 1
        tmp >>= 1
        nans = ans + self.divide(dividend - tmp,divisor)
        if ispositive:
            if ans > 2147483647:
                return 2147483647
            return nans
        if ans >= 2147483648:
            return -2147483648
        return 0 - nans
                