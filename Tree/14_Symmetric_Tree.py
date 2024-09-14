from math import e


class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None


    def levelOrder2(self):
        root = self
        queue = [root]
        result = []
        while len(queue) != 0:
            element = queue.pop(0)
            result.append(element.val)
            if element.lchild:
                print("left -> ",element.lchild.val)
                queue.append(element.lchild)
            if element.rchild:
                print("right -> ",element.rchild.val)
                queue.append(element.rchild)
        # print(result)

    def isSymmetric(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
    
        
        return ( root1.val == root2.val and self.isSymmetric(root1.lchild,root2.rchild) and self.isSymmetric(root1.rchild,root2.lchild))

    def symmetric_tree(self):
        if self is None:
            print("BT is empty")
            return
        else:
            value = self.isSymmetric(self.lchild,self.rchild)
            print(value)
            return






root = BST(1)
root.lchild = BST(2)
root.rchild = BST(3)
root.lchild.lchild = BST(3)
root.lchild.rchild = BST(4)
root.rchild.lchild = BST(4)
root.rchild.rchild = BST(3)
root.symmetric_tree()
