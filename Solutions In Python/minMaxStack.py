class minMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []
    
    def peep(self):
        return self.stack[len(self.stack) - 1]
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
        
    def push(self, number):
        self.stack.append(number)
        if len(self.minMaxStack) == 0:
            self.minMaxStack.append((number, number))
        else:
            maxi, mini = self.minMaxStack[-1]
            maxi = max(number, maxi)
            mini = min(number, mini)
            self.minMaxStack.append((maxi, mini))
        
        return


    def getMin(self):
        if len(self.minMaxStack) == 0:
            return None
        else:
            return self.minMaxStack[-1][1]
    def getMax(self):
        if len(self.minMaxStack) == 0 :
            return None
        else:
            return self.minMaxStack[-1][0]