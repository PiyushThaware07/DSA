class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

    def insert_node(self, data):
        if self.val is None:
            self.val = data
            return

        if data < self.val:
            if self.lchild is not None:
                self.lchild.insert_node(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insert_node(data)
            else:
                self.rchild = BST(data)

    def height(self):
        if self is None or self.val is None:
            return 0
        lh = self.lchild.height() if self.lchild else 0
        rh = self.rchild.height() if self.rchild else 0
        return 1 + max(lh, rh)

    def diameter(self):
        result = [0]
        if self.val == None:
            return 0
        
        lh = self.lchild.height() if self.lchild else 0
        rh = self.rchild.height() if self.rchild else 0
        result[0] = max(result[0],lh+rh)
        return 1+max(lh,rh)



# Example usage
root = BST(None)
nums = [5,10,7,15,12,20,25,22,28,30]
for num in nums:
    root.insert_node(num)

print(f"Diameter of the tree is: {root.diameter()}")
