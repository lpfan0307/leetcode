class Solution(object):
    def is_valid(self,par_num,right_num,position):
        left_num = position+1-right_num
        if left_num>=right_num and left_num<=par_num:
            return True
        return False
    def backtrack(self,position,result,par_num,pars,right_count,combines,end_num):
        if position == end_num:
            combines.append(''.join(result))
            return
        for i in range(2):
            result[position]=pars[i]
            right_count+=i
            if self.is_valid(par_num, right_count,position):
                self.backtrack(position+1,result,par_num,pars,right_count,combines,end_num)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        par_num = n
        result = ['']*par_num*2
        pars = ['(',')']
        combines = []
        self.backtrack(0, result, par_num,pars,0,combines,par_num*2)
        # print(combines)
        return combines
