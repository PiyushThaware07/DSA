class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if data < self.key:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        elif data > self.key:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
        else:
            print(f"~> {data} already exists in the BST.")
    
    def traversal(self):
        def inorder(node):  # Left | Root | Right
            if node is not None:
                inorder(node.left)
                print(node.key, end=' ')
                inorder(node.right)
        
        def preorder(node):  # Root | Left | Right
            if node is not None:
                print(node.key, end=' ')
                preorder(node.left)
                preorder(node.right)
        
        def postorder(node): # Left | Right | Root
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                print(node.key, end=' ')
        
        print("Inorder Traversal:")
        inorder(self)
        print("\nPreorder Traversal:")
        preorder(self)
        print("\nPostorder Traversal:")
        postorder(self)
        print()
    
    def delete(self, data):
        if self.key is None:
            print("~> BST is empty")
            return self
        
        if data < self.key:
            if self.left is not None:
                self.left = self.left.delete(data)
            else:
                print("~> Given Node is not present in tree.")
        elif data > self.key:
            if self.right is not None:
                self.right = self.right.delete(data)
            else:
                print("~> Given node is not present in tree")
        else:
            # CASE ~> Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # CASE ~> Node with two children: Get the inorder successor
            successor = self.right
            while successor.left:
                successor = successor.left
            
            self.key = successor.key
            self.right = self.right.delete(successor.key)
        
        return self

# Example Usage
root = BST(None)
nums = [10, 5, 20, 15, 18, 30, 25, 22, 24]
for num in nums:
    root.insert(num)

print("Before deletion:")
root.traversal()

root.delete(20)
root.delete(25)
root.delete(5)

print("\nAfter deletion:")
root.traversal()
