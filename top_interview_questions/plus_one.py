class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]<=8:
            digits[-1]+=1
            return digits
        digits[-1]=0
        carray_bit = 1
        for i in range(1,len(digits)):
            index = len(digits)-1-i
            digits[index] = digits[index]+carray_bit
            if digits[index]==10:
                digits[index]=0
                carray_bit=1
            else:
                return digits
        if carray_bit:
            digits.insert(0,1)
        return digits
