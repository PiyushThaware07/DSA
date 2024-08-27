from numpy import delete


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
    
    def delete(self, target):
        if self.key is None:
            print("~> BST is empty")
            return
        
        if target < self.key:
            if self.left is not None:
                self.left = self.left.delete(target)
            else:
                print("~> Given target node is not found in BST.")
                return
        elif target > self.key:
            if self.right is not None:
                self.right = self.right.delete(target)
            else:
                print("~> Given target node is not present in BST.")
                return
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.right
                self = None
                return temp
            else:
                node = self.right
                while node.left is not None:
                    node = node.left
                self.key = node.key
                self.right = self.right.delete(node.key)
        return self


# Example Usage
root = BST(None)
nums = [10, 5, 20, 15, 18, 30, 25, 22, 24]
for num in nums:
    root.insert(num)
print("\n Before Deletion")
root.traversal()

print("\n After Deletion")
root.delete(20)
root.delete(5)
root.traversal()