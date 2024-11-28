class BST:
    def __init__(self,key):
        self.lchild = None
        self.key = key
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
        else:
            if data < self.key:
                if self.lchild is None:
                    self.lchild = BST(data)
                else:
                    self.lchild.insert(data)
            else:
                if self.rchild is None:
                    self.rchild = BST(data)
                else:
                    self.rchild.insert(data)
    
    def search(self,target):
        if self.key is None:
            print("BST is empty!")
            return
        if self.key == target:
            print("Node Found!")
            return
        if target < self.key:
            if self.lchild is not None:
                self.lchild.search(target)
            else:
                print("Not Found!")
                return
        else:
            if self.rchild is not None:
                self.rchild.search(target)
            else:
                print("Not Found!")
                return
    
    def preOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        print(self.key,end=" ")
        if self.lchild is not None:
            self.lchild.preOrder()
        if self.rchild is not None:
            self.rchild.preOrder()
    
    def postOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.postOrder()
        if self.rchild is not None:
            self.rchild.postOrder()
        print(self.key,end=" ")
    
    def inOrder(self):
        if self.key is None:
            print("BST is empty!")
            return
        if self.lchild is not None:
            self.lchild.inOrder()
        print(self.key,end=" ")
        if self.rchild is not None:
            self.rchild.inOrder()
        
    def delete(self,target):
        # 1. check for tree empty
        if self.key is None:
            print("BST is empty!")
            return
        # 2. find the node
        if target < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(target)
            else:
                print("Given node is not present in current BST!")
                return
        elif target > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.delete(target)
            else:
                print("Given node is not present in current BST!")
                return
        else:
            # Delete node having 0 & 1 children's
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            '''
            Delete node having 2 childrens : 
            CASE 1 : Either take the largest node from the left subtree so that if should be largest from right.
            CASE 2 : Else take the smallest node from the right subtree, but i right subtree it is present on the left side of right subtree
            '''
            # I was following : Case 02
            node = self.rchild
            while node.lchild is not None:
                node = node.lchild
            self.key = node.key # Copy node value
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def countNode(self):
        if self is None:
            return 0
        leftCount = self.lchild.countNode() if self.lchild is not None else 0
        rightCount = self.rchild.countNode() if self.rchild is not None else 0
        print("Left Count : ",leftCount,"Right Count : ",rightCount,"Total Count : ",1 + leftCount + rightCount)
        return 1 + leftCount + rightCount
    
    def minValueNode(self):
        if self.lchild is None:
            print(self.key)
            return
        else:
            current = self
            while current.lchild is not None:
                current = current.lchild
            print(current.key)
            return
    
    def maxValueNode(self):
        if self.rchild is None:
            print(self.key)
            return
        else:
            current = self
            while current.rchild is not None:
                current = current.rchild
            print(current.key)
            return
            
            
    def levelOrder(self):
        root = self
        queue = [root]
        result = []
        while queue:
            levelSize = len(queue)
            levelNodes = []
            for _ in range(levelSize):
                current = queue.pop(0)
                levelNodes.append(current.key)
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)
            result.append(levelNodes)
        print(result)
        return
    
    
    def HeightOfBST(self):
        root = self
        queue = [root]
        height = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                current = queue.pop(0)
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)
            height = height + 1
        print(height)
        
    
    def findDepth(self):
        if self.key is None:
            return 0
        
        leftHeight = 0
        rightHeight = 0
        if self.lchild is not None:
            leftHeight = self.lchild.findDepth()
            if leftHeight == -1:
                return -1
        if self.rchild is not None:
            rightHeight = self.rchild.findDepth()
            if rightHeight == -1:
                return -1
        if abs(leftHeight-rightHeight) > 1:
            return -1
        return max(leftHeight,rightHeight) + 1
        
    def isBalanced(self):
        if self.findDepth() == -1:
            print("Unbalanced")
        else:
            print("Balanced")
            
        
                    

root = BST(None)
nums = [10,7,12,6,5,17,8,16]
for num in nums:
    root.insert(num)
root.isBalanced()