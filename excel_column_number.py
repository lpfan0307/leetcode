class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        s = s[::-1]
        number = 0
        mag= 1

        for i in range(len(s)):
            number+=mag*(ord(s[i])-ord('A')+1)
            mag*=26
        return number
