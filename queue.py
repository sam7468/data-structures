# queue size remains same
class Queue:
    def __init__(self): 
        self.queue = [] 
        self.front  = 0 #remove @
        self.rear = -1  #insert @

    def push(self,val):
        self.rear+=1
        self.queue.insert(self.rear,val)

    def pop(self):
        print(self.queue[self.front])
        self.front +=1 

    def printq(self):
        print(self.queue[self.front:self.rear+1])    

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.pop()
queue.pop()
queue.printq()


