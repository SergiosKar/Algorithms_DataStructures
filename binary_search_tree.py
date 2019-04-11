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

    def insert(self,newValue):
        self._insertNode(newValue,self.head)
    
    def _insertNode(self,newValue,parentNode):

        if(parentNode is None):
            parentNode=self.head
        else:
            if(newValue<parentNode.value):
                if(parentNode.left is None):
                    parentNode.left=Node(newValue)
                else:
                    self._insertNode(newValue,parentNode.left)
            else:
                if(parentNode.right is None):
                    parentNode.right=Node(newValue)
                else:
                    self._insertNode(newValue,parentNode.right)

    def search(self,value):
        self.result=None
        self._search(value,self.head)
        return self.result

    def _search(self,value,parentNode):
        if(parentNode is None):
            return 
        else:
            if(value<parentNode.value):
                self._search(value,parentNode.left)
            elif(value>parentNode.value):
                self._search(value,parentNode.right)
            else:
                print(str(parentNode.value) +' is found')
                self.result=parentNode

    def inOrder_traversal(self):
        yield from self._inorder(self.head)

    def _inorder(self,parent):
        if(parent is not None):
            yield from self._inorder(parent.left)
            yield parent.value
            yield from self._inorder(parent.right)

    def inorder_iter(self):
        root=self.head
        stack=[]
        res=[]

        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            
            root=stack.pop()
            res.append(root.value)

            root=root.right

        return res

    
    def preorder_traversal(self):
        self._preorder(self.head)

    def _preorder(self,parent):
        if(parent is not None):
            print(parent.value)
            self._preorder(parent.left)
            self._preorder(parent.right)

    def preorder_iter(self):
        root=self.head
        stack=[root]
        res=[]

        while stack:

            root=stack.pop()
            if root:
                res.append(root.value)
                stack.append(root.right)
                stack.append(root.left)           


        return res


    def postorder_traversal(self):
            self._postorder(self.head)

    def _postorder(self,parent):
        if(parent is not None):
            self._postorder(parent.left)
            self._postorder(parent.right)
            print(parent.value)
    
    def postorder_iter(self):
        root=self.head
        stack=[root]
        res=[]

        while stack:

            root=stack.pop()
            if root:
                res.append(root.value)
                stack.append(root.left)
                stack.append(root.right)           

        res.reverse()
        return res

    def dft(self,value):
        self.search(value)
        self._depth_first_traversal(self.result)
    def _depth_first_traversal(self,node):
        if node is not None:
            print(node.value)
            self._depth_first_traversal(node.left)
            self._depth_first_traversal(node.right)

   
        




            

btree=Btree(30)

btree.insert(10)
btree.insert(20)
btree.insert(25)
btree.insert(40)
btree.insert(50)



# btree.dft(30)

# btree.printTree()
#btree.search(10)
# btree.inOrder_traversal()
# for i in btree.inOrder_traversal():
#     print(i)
btree.postorder_traversal()

btree.postorder_iter()

