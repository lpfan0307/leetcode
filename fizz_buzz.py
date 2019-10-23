class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            value = str(i)
            if i % 15 == 0 :
                value = 'FizzBuzz'
            elif i % 3 == 0:
                value = 'Fizz'
            elif i % 5 == 0:
                value = 'Buzz'
            result.append(value)
        return result
