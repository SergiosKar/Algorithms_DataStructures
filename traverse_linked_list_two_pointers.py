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



def traverse_with_two_pointers(left,right):

    if right is None:
        return left

    left=traverse_with_two_pointers(left,right.nextNode)
    print(left.value,right.value)        
    left=left.nextNode
    
    return left
    
traverse_with_two_pointers(n1,n1)