print("runnin....")

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Head:
    def  __init__(self):
        self.head= None

    def getlen(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next    
        print("len - " + str(count))
        return count    

    def addtoFront(self,val): #can be used as stack
        if not self.head:
            node = Node(val,None)
            self.head = node #just make a head
        else:
            node = Node(val,self.head)
            self.head = node #make a node pointing to head & make head as our new node

    def addtoEnd(self,val):
        node = Node(val,None)
        if not self.head:
            self.head = node
        else:    
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node  
              
    def show(self):
        if self.head == None:
            print("Empty LinkedList")
            return
        else:
            ll = ""
            temp = self.head 
            while temp:
                ll += ("{}".format(temp.val) + "-->")
                temp = temp.next
            print(ll) 

    def insertatindex(self,idx,val):
        if idx > self.getlen():
            print("invalid idx")
            return 
        else:
            temp = self.head
            for i in range(idx-1):
                temp = temp.next
            node = Node(val,temp.next)
            temp.next = node        

run = Head()
run.addtoFront("node")
run.addtoFront(20)
run.addtoFront(30)
run.addtoEnd(30)
run.addtoEnd(20)
run.insertatindex(3,"inserted-Node")
run.show()



#    30-->  20 --> 10 --> 20--> 30 -->





        

