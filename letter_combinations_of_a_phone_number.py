class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        result = []
        for key in dic:
            l = dic[key]
            l.sort()
            result.append(l)
        return result
