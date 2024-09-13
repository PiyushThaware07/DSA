from turtle import left


class BST:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None
    
    def insert_node(self,data):
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
        if self.val is None:
            return 0
        
        lh = 0
        rh = 0
        if self.lchild is not None:
            lh = self.lchild.diameter()
        
        if self.rchild is not None:
            rh = self.rchild.diameter()

        return 1 + max(lh,rh)
    
    def diameter(self):
        if self.val is None:
            return 0
        
        lh = self.height(self.lchild)
        rh = self.height(self.rchild)

        ld = self.diameter(self.lchild)
        rd = self.diameter(self.rchild)
        






root = BST(None)
# nums = [10,5,7,15,20,17,25]
nums = [1, 2, 3, 4, 5, 6,7]
for num in nums:
    root.insert_node(num)
root.diameter()