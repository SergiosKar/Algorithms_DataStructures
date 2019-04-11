class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None

n1=Node(5)
n2=Node(6)
n3=Node(7)
n4=Node(8)

n1.nextNode=n2
n2.nextNode=n3
n3.nextNode=n4

#traverse and print
def traverse(head):
    n=head
    while n is not None:
        print(n.value)
        n=n.nextNode

traverse(n1)
#reverse 
def reverse(n):
    prev=None
    current = n 
    while(current is not None): 
        next = current.nextNode
        current.nextNode = prev 
        prev = current 
        current = next
    head = prev 
    return head

head=reverse(n1)

traverse(head)

#insert
newNode=Node(8)
n=n1
while n is not None:
    if(n.nextNode is None):
        n.nextNode=newNode
        break
    n=n.nextNode

#delete
deleteNode_value=7
currentNode=n1
previousNode=None
while currentNode  is not None:
    if(currentNode.value==deleteNode_value):
        if(previousNode is None):
            currentNode.nextNode=None
            break
        previousNode.nextNode=currentNode.nextNode
        break
    previousNode=currentNode
    currentNode=currentNode.nextNode

def traverse_backwards(n):

    if n is None:
        return

    traverse_backwards(n.nextNode)
    print(n.value)        

traverse_backwards(n1)