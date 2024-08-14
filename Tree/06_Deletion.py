class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if data <= self.key:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    def preorder(self):
        result = []
        def traversal(node):
            if node is None:
                return 
            result.append(node.key)
            traversal(node.left)
            traversal(node.right)
        traversal(self)
        print("Preorder --> ",result)


    # ! deletion
    def delete(self, target):
        # Tree is empty
        if self.key is None:
            print("~> BST is empty")
            return self
        
        # Search in the left subtree
        if target < self.key:
            if self.left is not None:
                self.left = self.left.delete(target)
            else:
                print("~> Node not found")
        
        # Search in the right subtree
        elif target > self.key:
            if self.right is not None:
                self.right = self.right.delete(target)
            else:
                print("~> Node not found")
        
        # Node to be deleted found (target == self.key)
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            
            if self.right is None:
                temp = self.left
                self = None
                return temp
            
            # Node with two children: get the inorder successor (smallest in the right subtree)
            temp = self.right
            while temp.left is not None:
                temp = temp.left
            
            # Copy the inorder successor's content to this node
            self.key = temp.key
            
            # Delete the inorder successor
            self.right = self.right.delete(temp.key)
        
        print(self)




            



        





root = BST(None)
nums = [1,4,2,0,45,32,56,7,54,3]
for num in nums:
    root.insert(num)
root.preorder()
root.delete(2)
root.preorder()