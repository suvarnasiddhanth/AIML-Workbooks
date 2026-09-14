class Stack:
    def __init__(self,val=None, maxsize=None):
        self.value = []
        self.top = -1 if val == None else 0
        self.value.append(val)
        self.maxsize = maxsize
    def __repr__(self):
        return f"{self.value}"
    def push(self,val):
        if self.isFull() == True:
            return
        else:
            self.value.append(val)
            self.top += 1
    def pop(self):
        if self.isEmpty() == True:
            return
        else:
            self.value.pop()
            self.top -= 1
    def peek(self):
        if self.isEmpty() != True: 
            print(self.value[self.top])
    def size(self):
        return (self.top + 1)
    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty.")
            return True
    def isFull(self):
        if self.top == (self.maxsize - 1):
            print("Stack is full.")
            return True
s = Stack("Hello", 5)
s.push("World,")
s.push(42)
s.push("is")
print(s)
s.pop()
s.peek()
print("Size of stack:",s.size())
s.push("is")
s.push("the")
s.push("secret")
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.peek()
s.pop()