class BST:
    def __init__(self,key):
        self.lchild = None
        self.key = key
        self.rchild = None
    
    def insert(self,data):
        # CASE 1 : Tree Empty (insert at the root of tree)
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        # CASE 2 : Tree not empty
        if self.key > data:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insert(data)
                
    
    def search(self,target):
        if self.key is None:
            print("BST is empty!")
            return
        # CASE 1 : Root is target
        if target == self.key:
            print("Found Successfully!")
            return
        # CASE 2 : Search target in left subtree
        if target < self.key:
            if self.lchild is None:
                print("Not not found!")
                return
            else:
                self.lchild.search(target)
        else:
            if self.rchild is None:
                print("Node not found!")
                return
            else:
                self.rchild.search(target)
    
    def preOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        print(self.key,end=" ")
        if self.lchild is not None:
            self.lchild.preOrder()
        if self.rchild is not None:
            self.rchild.preOrder()
    
    def inOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.inOrder()
        print(self.key,end=" ")
        if self.rchild is not None:
            self.rchild.inOrder()
    
    def postOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.postOrder()
        if self.rchild is not None:
            self.rchild.postOrder()
        print(self.key,end=" ")
        
            
            
            
        
        

root = BST(None)
nums = [10,7,12,6,5,17,12,8,16,20]
for num in nums:
    root.insert(num)
root.search(17)
root.preOrder()
print("\n")
root.inOrder()
print("\n")
root.postOrder()