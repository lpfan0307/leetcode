class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        num_squre = {}
        for i in range(1,n+1):
            num = i**2
            if num>n:
                break
            nums.append(num)
            num_squre[num] = 1 
        
        num_squre[0] = 0
        num_squre[1] = 1
        for i in range(2, n+1):
            min_num = n
            for num in nums:
                if i<num:
                    break
                cur_count = 1+num_squre[i-num]
                if min_num > cur_count:
                    min_num = cur_count
            num_squre[i] = min_num
        return num_squre[n]

s = Solution()
print(s.numSquares(0))