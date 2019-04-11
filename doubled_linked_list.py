class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None
        self.prevNode=None


class doubled_linked_list:

    def __init__(self,headNode):
        self.headNode=headNode

    def push(self,newNode_value):
        newNode=Node(newNode_value)

        current_node=self.headNode
        while current_node.nextNode is not None:
            current_node=current_node.nextNode
        current_node.nextNode=newNode
        newNode.prevNode=current_node
    
    def traverse(self):
        current_node=self.headNode
        print(self.headNode.value)
        while current_node.nextNode is not None:
            current_node=current_node.nextNode
            print(current_node.value)

    def insert(self,previousvalue,value):

        newNode=Node(value)
        
        current_node=self.headNode
        while True:
            if(current_node.value==previousvalue):
            
                newNode.prevNode=current_node
                newNode.nextNode=current_node.nextNode
                current_node.nextNode.prevNode=newNode
                current_node.nextNode=newNode
                return    
            current_node=current_node.nextNode

            if current_node.nextNode is  None:
                if(current_node.value==previousvalue):
                    current_node.nextNode=newNode
                    newNode.prevNode=current_node
                    break
                else:
                    break

        
        
dll=doubled_linked_list(Node(1))

dll.push(2)
dll.push(3)

dll.traverse()

dll.insert(13,13)