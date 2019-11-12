class Solution(object):
    def is_palindrome(self, s):
        num = len(s)
        for i in range(int(num)/2):
            if s[i] != s[num-i-1]:
                return False
        return True
    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.res.append(stringlist)
        for i in range(1,len(s)+1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.dfs(s, [])
        return Solution.res