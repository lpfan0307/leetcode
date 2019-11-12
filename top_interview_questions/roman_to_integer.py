class Solution:
    # @return an integer
    def romanToInt(self, s):
        digits = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        len_s = len(s)
        num = 0
        for i in range(0, len_s - 1):
            cur = digits[s[i]]
            next = digits[s[i + 1]]
            if cur >= next:
                num += cur
            else:
                num -= cur
        num += digits[s[len_s - 1]]
        return num
