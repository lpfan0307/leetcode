class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            #print(stack)
            #print(each)
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()

                    if top < 0:
                        stack.append(-1*int(-1*top / num))
                    else:
                        stack.append(int(top / num))
                pre_op = each
                num = 0

        return sum(stack)
s = Solution()
s.calculate("14-3/2")