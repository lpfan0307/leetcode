class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        size = len(s)
        f = [False]*(size+1)
        if size ==0:
            return False
        f[-1]=True
        for i in range(size-1,-1,-1):
            for j in range(i+1,size+1):

                f[i] = (s[i:j] in wordDict) and f[j]
                if f[i]:
                    break
        return f[0]

