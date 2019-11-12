class Solution(object):
    def parse_list(self, l):
        result = []
        count = 1
        last_v = l[0]
        for i in l[1:]:
            if i == last_v:
                count += 1
            else:
                result.append(count)
                result.append(last_v)
                count = 1
                last_v = i
        result.append(count)
        result.append(last_v)
        return result
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = [1]
        if n == 1:
            s = [str(item) for item in s]
            return ''.join(s)
        for i in range(1,n):
            s = self.parse_list(s)
        s = [str(item) for item in s]
        return ''.join(s)