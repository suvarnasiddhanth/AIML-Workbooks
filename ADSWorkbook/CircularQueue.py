#Parially done
class Queue:
    def __init__(self, val = None, maxsize = None):
        self.value = []
        if val != None: 
            self.value.append(val)
            self.currsize = 1
        else:
            self.currsize = 0
        self.maxsize = maxsize
        self.start = 0
        self.end = 0
    def __repr__(self):
        if self.start < self.end:
            return f"{self.value[self.start:]}"
        else:
            return f"{self.value[self.start].extend(self.value[:self.end])}"
    def size(self):
        return self.currsize
    def enqueue(self,val):
        if self.isFull() != True:
            self.value.append(val)
            self.currsize += 1
            self.end += 1
        else:
            print("Increasing size of queue...")
            self.maxsize *= 2
            self.currsize += 1
            self.end += 1
    def dequeue(self):
        if self.isEmpty() != True:
            self.value[self.start] = None
            self.currsize -= 1
            self.start += 1
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
q.enqueue([6,3,4])
q.enqueue(2)
q.enqueue("d")
q.enqueue(print)
q.dequeue()
q.enqueue(globals)
q.enqueue(3)
print(q)