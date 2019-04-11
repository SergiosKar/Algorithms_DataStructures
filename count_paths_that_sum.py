class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=None

class Btree:
    def __init__(self,head_value):
        self.head=Node(head_value)

    def printTree(self):
        self._printTree(self.head)

    def _printTree(self,parentNode):

        if(parentNode is not None):
            if parentNode.left is not None:
                self._printTree(parentNode.left)
            print( parentNode.value),
            if parentNode.right is not Node:
                self._printTree(parentNode.right)
            
        
    def inOrder_traversal(self):
        self._inorder(self.head)

    def _inorder(self,parent):
        if(parent is not None):
            self._inorder(parent.left)
            print(parent.value)
            self._inorder(parent.right)

    
    def preorder_traversal(self):
        self._preorder(self.head)

    def _preorder(self,parent):
        if(parent is not None):
            print(parent.value)
            self._preorder(parent.left)
            self._preorder(parent.right)

    def postorder_traversal(self):
            self._postorder(self.head)

    def _postorder(self,parent):
        if(parent is not None):
            self._postorder(parent.left)
            self._postorder(parent.right)
            print(parent.value)


    def sumPaths(self,node,cur_sum,sum,count):

        if node is None:
            return count
           
        cur_sum+=node.value
        if cur_sum==sum:
            count+=1

        
                
        cnt1=self.sumPaths(node.left,cur_sum,sum,count)
        cnt2=self.sumPaths(node.right,cur_sum,sum,count)

        return cnt1+cnt2
   




            

btree=Btree(50)

btree.head.left=Node(20)
btree.head.right=Node(10)
btree.head.left.left=Node(10)
btree.head.left.right=Node(15)
btree.head.right.left=Node(13)
btree.head.right.right=Node(3)
btree.head.left.left.left=Node(5)
btree.head.left.left.right=Node(15)
btree.head.right.left.left=Node(2)
btree.head.right.left.right=Node(8)

#btree.printTree()
#btree.search(10)
#btree.inOrder_traversal()
# btree.postorder_traversal()
# btree.preorder_traversal()

btree.sumPaths(btree.head,0,75,0)



int('0011',2) <<2


int('11000011',2) << bin(1)


a=60
bin(a)

c=a<<2
bin(c)