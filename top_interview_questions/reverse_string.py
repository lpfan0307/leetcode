class Solution(object):
    def reverseString(self, s):
	str_len = len(s)
        for i in range(str_len/2):
            t = s[i]
            s[i] = s[str_len-i-1]
            s[str_len-i-1] = t
