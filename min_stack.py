class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.minStack.append(0)
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1][0] > x:
            #print 'minn change'
            self.minStack.append((x,1))
        elif x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)
 
    # @return nothing
    def pop(self):
        p = self.stack.pop()
        #print 'pop ' , p
        if p == self.minStack[-1][0]:
            if self.minStack[-1][1] > 1:
                #print 'minn pop'
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        #print self.minStack
        return self.minStack[-1][0]