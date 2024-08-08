class CreateNode:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    

# Create Root Child
root = CreateNode(100)
print(root.lchild,root.key,root.rchild)


# Creating Left Child
root.lchild = CreateNode(50)
print(root.lchild,root.key,root.rchild)
print(root.lchild.lchild,root.lchild.key,root.lchild.rchild)


# Creating Right Child
root.rchild = CreateNode(150)
print(root.lchild,root.key,root.rchild)
print(root.rchild.lchild,root.rchild.key,root.rchild.rchild)