class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(1,numRows+1):
            l.append([1]*i)
        for i in range(2,numRows):
            for j in range(1,i):
                l[i][j] = l[i-1][j-1]+l[i-1][j]
        return l
