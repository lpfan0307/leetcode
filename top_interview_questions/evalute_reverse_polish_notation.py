class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop( )
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '-':
                    stack.append(b-a)
                elif tokens[i] == '*':
                    stack.append(a*b)
                if tokens[i] == '/':
                    if a*b < 0:
                        stack.append(-((-b)/a))
                    else:
                        stack.append(b/a)
        return stack.pop()