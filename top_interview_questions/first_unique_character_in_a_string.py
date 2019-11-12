class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for idx,ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1