class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)
        print(b)

        # 不到32位,变成32位
        if len(b) < 34:
            b = '0b' + '0' * (34 - len(b)) + b[2:]

        print(b)
        reversed_b = "0b" + b[2:][::-1]

        return int(reversed_b, 2)


