
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
       
        intervals = sorted(intervals,key = lambda k:k[0])
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1],i[1])
            else:
                res.append(i)
        return res
