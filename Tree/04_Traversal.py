'''
Pre-Order Traversal   --> root | left  | right
In-Order Traversal    --> left | root  | right
Post-Order Traversal  --> left | right | root
'''
from turtle import right


class BST:
    def __init__(self,key):
        self.key = key
        self.leftNode = None
        self.rightNode = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if data <= self.key:
            if self.leftNode is not None:
                self.leftNode.insert(data)   # <-- Recursive call
            else:
                self.leftNode = BST(data)
        else:
            if self.rightNode is not None:
                self.rightNode.insert(data)  # <-- Recursive call
            else:
                self.rightNode = BST(data)
    
    # ! preorder Traversal --> root | left | right
    def preOrder(self):
        # Check if the tree is empty
        if self.key is None:
            print("~> Binary search tree is empty")
            return
        
        # Print the key of the current node
        print(self.key,end=" ")               # <-- root node

        # Visit the left subtree if it exists
        if self.leftNode is not None:
            self.leftNode.preOrder()          # <-- left node
        
        # Visit the right subtree if it exists
        if self.rightNode is not None:
            self.rightNode.preOrder()         # <-- right node
    

    # ! Inorder Traversal --> left | root | right
    def inOrder(self):
        # Check if the tree is empty
        if self.key is None:
            print("~> Binary search tree is empty")
            return
        
        # Visit the left subtree if it exists
        if self.leftNode is not None:
            self.leftNode.inOrder()           # <-- left node
        
        print(self.key,end=" ")                       # <-- root node

        # Visit the right subtree if it exists
        if self.rightNode is not None:
            self.rightNode.inOrder()          # <-- right node
        

    # ! postorder Traversal --> left | right | root
    def postOrder(self):
        # Check if the tree is empty
        if self.key is None:
            print("~> Binary search tree is empty")
            return
        
        # Visit the left subtree if it exists
        if self.leftNode is not None:
            self.leftNode.postOrder()        # <-- left node
        
        # Visit the right subtree if it exists
        if self.rightNode is not None:
            self.rightNode.postOrder()       # <-- right node
        
        print(self.key,end=" ")              # <-- root node







root = BST(None)
nums = [10,5,3,20,43,37,58,100]
for num in nums:
    root.insert(num)
# root.preOrder()
# root.inOrder()
root.postOrder()