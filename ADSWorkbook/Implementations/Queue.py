class Queue:
    def __init__(self, val = None, maxsize = None):
        self.value = []
        if val != None: 
            self.value.append(val)
            self.currsize = 1
        else:
            self.currsize = 0
        self.maxsize = maxsize
    def __repr__(self):
        return f"{self.value}"
    def size(self):
        return self.currsize
    def enqueue(self,val):
        if self.isFull() != True:
            self.value.append(val)
            self.currsize += 1
    def dequeue(self):
        if self.isEmpty() != True:
            self.value = self.value[1:]
            self.currsize -= 1
    def peek(self):
        if self.isEmpty() != True: print("Peek value:", self.value[0])
    def isFull(self):
        if self.currsize == self.maxsize:
            print("Queue is full.")
            return True
    def isEmpty(self):
        if self.currsize == 0:
            print("Queue is empty.")
            return True
q=Queue(None,5)
q.peek()
q.enqueue([6,3,4])
q.enqueue(2)
q.enqueue("d")
q.enqueue(print)
q.enqueue(globals)
q.enqueue(3)
print(q)