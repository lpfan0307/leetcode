class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in xrange(rows / 2):
                for j in xrange(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in xrange(rows):
                for j in xrange(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
