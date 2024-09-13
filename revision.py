class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert_node(self, data):
        # If BST is empty, insert the first node
        if self.key is None:
            self.key = data
            return
        
        # Insert data in the correct position
        if data < self.key:
            if self.left is not None:
                self.left.insert_node(data)
            else:
                self.left = BST(data)
        elif data > self.key:
            if self.right is not None:
                self.right.insert_node(data)
            else:
                self.right = BST(data)

    def pre_order(self):  # root | left | right
        if self.key is None:
            print("~> BST is empty")
            return
        
        print(self.key,end=" ")
        if self.left is not None:
            self.left.pre_order()
        
        if self.right is not None:
            self.right.pre_order()

    def post_order(self):  # left | right | root
        if self.key is None:
            print("~> BST is empty")
            return
        
        if self.left is not None:
            self.left.post_order()
        
        if self.right is not None:
            self.right.post_order()

        print(self.key,end=" ")
    
    
    def in_order(self):  # root | left | right
        print(self.key,end=" ")

        if self.left is not None:
            self.left.in_order()
        
        if self.right is not None:
            self.right.in_order()
        
    def search(self,target):
        if target == self.key:
            print("~> target found")
            return
        
        if target < self.key:
            if self.left is not None:
                self.left.search(target)
            else:
                print("~> target not found")
                return
        else:
            if self.right is not None:
                self.right.search(target)
            else:
                print("~> target not found")
                return


    def level_order_traversal(self):
        if self.key is None:
            print("~> BST is empty")
            return
        
        queue = [self]  # Start with the root node (self)
        while len(queue) != 0:
            root = queue.pop(0)  # Pop the first node from the queue
            print(root.key, end=" ")  # Print the key of the current node

            # Add the left child if it exists
            if root.left is not None:
                queue.append(root.left)
            
            # Add the right child if it exists
            if root.right is not None:
                queue.append(root.right)




root = BST(None)
nums = [10,5,7,15,12,17,20]
for num in nums:
    root.insert_node(num)
# root.pre_order()
# root.post_order()
# root.in_order()

# root.search(2)
root.level_order_traversal()