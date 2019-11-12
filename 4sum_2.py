class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        dicA,dicB,dicC,dicD = Counter(A),Counter(B),Counter(C),Counter(D)
        res = 0
        dic = {}
        for a , a_nember in dicA.items():
            for b, b_nember in dicB.items():
                dic[a+b] = dic.get(a+b,0) + a_nember * b_nember
        for c, c_nember in dicC.items():
            for d, d_nember in dicD.items():
                res += dic.get(-c-d,0)*c_nember*d_nember
        return res