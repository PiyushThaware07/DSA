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

    def method01(self):
        if self is None:
            return [] # Return an empty list if the root is None
        
        queue = [self]
        result = []
        direction = False # False means left -> right, True means right -> left
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                
                 # Append the children of the current node to the queue
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)
            
            # Reverse the current level's order based on the direction
            if direction:
                result.append(current_level[::-1]) # Reverse the level for zigzag
            else:
                result.append(current_level[::])
            
            # Flip the direction for the next level
            direction = not direction
        print(result)
            





root = BST(1)
root.lchild = BST(2)
root.rchild = BST(3)
root.rchild.lchild = BST(4)
root.lchild.rchild = BST(5)
root.method01()
