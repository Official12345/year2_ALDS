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


def checkValid(s):
    for i in s:
        if i == '(' or i == '[' or i == '<':
            stack.push(i)
        elif i == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                stack.push(i)
        elif i == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                stack.push(i)
        elif i == '>':
            if stack.peek() == '<':
                stack.pop()
            else:
                stack.push(i)
    if stack.isEmpty():
        print("valid")
    else:
        print("invalid")

stack = mystack()
#string1 = "[(<>)]( )(( )( ))"
string1 = "()<>><)([]]][]())))"
checkValid(string1)


