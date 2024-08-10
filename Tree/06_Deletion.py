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

    # ! search
    def search(self,target):
        if self.key is None:
            print("~> BST is empty")
            return 
        
        if target == self.key:
            print("Node found")
            return
        
        if target <= self.key:
            if self.left is not None:
                self.left.search(target)
            else:
                print("~> Node not found")
        else:
            if self.right is not None:
                self.right.search(target)
            else:
                print("~> Node not found")

    # ! deletion
    def delete(self,target):
        # if bst is empty
        if self.key is None:
            print("~> BST is empty")
            return
        
        # target can be present in left either right sub-tree
        if target < self.key:
            if self.left is not None:
                self.left = self.left.delete(target)
                print(self.left)
            else:
                print("~> Node not found")
        elif target > self.key:
            if self.right is not None:
                self.right = self.right.delete(target)
                print(self.right)
            else:
                print("~> Node not found") 
        else:
            # 0 child or 1 child node deletion
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            
            # 2 child node deletion
            node = self.right  # find smallest node into the right sub-tree
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self 


        






root = BST(None)
nums = [1,4,2,0,45,32,56,7,54,3]
for num in nums:
    root.insert(num)
root.preorder()
root.delete(155)
root.preorder()