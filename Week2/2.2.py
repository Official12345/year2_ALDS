class mystack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) != 0:
            return self.data.pop(-1)

    def peek(self):
        if len(self.data) != 0:
            return self.data[-1]

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

s = mystack()
s.push(3)
s.push(5)
s.push(7)
print("peek:", s.peek())
print("first pop:",  s.pop())
print("second pop:", s.pop())
print(s.isEmpty())
s.pop()
print(s.isEmpty())
print(s.data)

