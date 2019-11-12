# class Solution(object):
#     def get_method_count(self, x,y):
     
#         if x==1 and y==2:
#             return 1
#         if x == 2 and y == 1:
#             return 1
#         if x == 1:
#             return self.get_method_count(1,y-1)
#         if y == 1:
#             return self.get_method_count(x-1,1)
#         return self.get_method_count(x-1,y) + self.get_method_count(x,y-1)
   
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         return self.get_method_count(m,n)

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            list = [[1]]
        elif m == 1 and n > 1:
            list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            list = [[1] for i in range(m)]
        else:
            list = [[0 for i in range(n)] for i in range(m)]
            for i in range(0, n):
                list[0][i] = 1
            for i in range(0, m):
                list[i][0] = 1
            for i in range(1, m):
                for j in range(1, n):
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1]

s = Solution()
s.uniquePaths(3,2)