class Stack:
    def __init__(self):
        self.stc = []
        self.top = -1

    def push(self,val):
        self.top +=1  #top keep moving with insert
        self.stc.insert(self.top , val)
        
    def pop(self):
        try:
            temp = self.stc[self.top]
            print(temp)
            self.top -= 1 #top always remember pos 
        except Exception as e:
            print(e)

    def printstc(self):
        print(self.stc[:self.top+1]) #print till the top-1 pos   

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.push("new " + str(3))
stack.push("new " + str(4))

stack.printstc()