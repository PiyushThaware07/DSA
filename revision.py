class BST:
    def __init__(self,key):
        self.key = key
        self.leftNode = None
        self.rightNode = None
    
    def insert(self,data):
        # insertion at root node
        if self.key is None:
            self.key = data
            return
        
        # insertion at the left sub-tree
        if self.key >= data:
            # left child already exists
            if self.leftNode is not None:
                self.leftNode.insert(data)
            else:
                self.leftNode = BST(data)
        else:
            # right child already exists
            if self.rightNode is not None:
                self.rightNode.insert(data)
            else:
                self.rightNode = BST(data)
    
    def inorder(self):  # LEFT | ROOT | RIGHT
        if self is None or self.key is None:
            print("~> BST is empty")
            return
        
        if self.leftNode is not None:
            self.leftNode.inorder()
        
        print(self.key)

        if self.rightNode is not None:
            self.rightNode.inorder()

    def preorder(self):  # ROOT | LEFT | RIGHT
        if self is None or self.key is None:
            print("~> BST is empty")
            return
        
        print(self.key)

        if self.leftNode is not None:
            self.leftNode.preorder()
        
        if self.rightNode is not None:
            self.rightNode.preorder()
        

    
    def postorder(self): # LEFT | RIGHT | ROOT
        if self is None or self.key is None:
            print("~> BST is empty")
            return
        
        if self.leftNode is not None:
            self.leftNode.postorder()
        
        if self.rightNode is not None:
            self.rightNode.postorder()
        
        print(self.key)

    def search(self,target):
        if self.key is None:
            print("~> BST is empty")
            return
        
        if self.key == target:
            print(f"Found")
            return
        
        if target <= self.key:
            if self.leftNode is not None:
                self.leftNode.search(target)
            else:
                print("~> Node not found")
                return
        else:
            if self.rightNode is not None:
                self.rightNode.search(target)
            else:
                print("~> Node not found")
                return








root = BST(100)
nodes = [200,150,250,300,350,400,450,500]
for node in nodes:
    root.insert(node)
# root.inorder()
# root.postorder()
# root.preorder()
root.search(250)