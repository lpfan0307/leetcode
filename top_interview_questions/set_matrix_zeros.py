class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rownum = len(matrix)
        colnum = len(matrix[0])
        rows = [False for i in range(rownum)]
        cols = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0