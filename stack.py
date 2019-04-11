class Stack:
    def __init__(self):
        self.stack=[]

    def insert(self,new_elem):
        self.stack.append(new_elem) # self.stack.insert(0,new_elem) in queue

    def delete(self):
        self.stack.pop()

    def search(self,el):

        for i in range(1,len(self.stack)):
            if(self.stack[i]==el):
                return i
            
        return -1


s=Stack()
s.insert(1)
s.insert(2)
s.insert(3)

s.search(2)

print(s.stack)

