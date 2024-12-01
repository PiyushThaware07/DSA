class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
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
    
    def traversal(self):
        if self.key is None:
            print("BST is empty")
        
        preResult = []    
        def preOrder(node):
            preResult.append(node.key)
            if node.lchild is not None:
                preOrder(node.lchild)
            if node.rchild is not None:
                preOrder(node.rchild)
        preOrder(self)
        print("Pre-order : ",preResult)
        
        inResult = []
        def inOrder(node):
            if node.lchild is not None:
                inOrder(node.lchild)
            inResult.append(node.key)
            if node.rchild is not None:
                inOrder(node.rchild)
        inOrder(self)
        print("In-order : ",inResult)
        
        
        postResult = []
        def postOrder(node):
            if node.lchild is not None:
                postOrder(node.lchild)
            if node.rchild is not None:
                postOrder(node.rchild)
            postResult.append(node.key)
        postOrder(self)
        print("Post-order : ",postResult)
        
        
       # Level-order Traversal
        def levelOrder(node):
            queue = [node]
            result = []
            while queue:
                currentNode = queue.pop(0)
                result.append(currentNode.key)
                if currentNode.lchild:
                    queue.append(currentNode.lchild)
                if currentNode.rchild:
                    queue.append(currentNode.rchild)
            print("Level-order:", result)
        levelOrder(self)
        
        
        def verticalOrder(node,hDist,vDist,hashMap):
            if hDist not in hashMap:
                hashMap[hDist] = [node.key]
            else:
                hashMap[hDist].append(node.key)
            if node.lchild is not None:
                verticalOrder(node.lchild,hDist-1,vDist+1,hashMap)
            if node.rchild is not None:
                verticalOrder(node.rchild,hDist+1,vDist+1,hashMap)
            
        def verticalTraversal(node):
            hashMap = {}
            verticalOrder(node,0,0,hashMap)
            sortHashMap = sorted(hashMap.items())
            result = []
            for hDist,data in sortHashMap:
                temp = [item for item in data]
                result.extend(temp)
            print(result)
        verticalTraversal(self)
    
    def findMinAndMax(self):
        if self is None:
            print("BST is empty!")
            return
        def minNode(node):
            if node.lchild is None:
                print(node.key)
                return
            else:
                currentNode = node
                while currentNode.lchild is not None:
                    currentNode = currentNode.lchild
                print(currentNode.key)
        minNode(self)
        
        def maxNode(node):
            if node.rchild is None:
                print(node.key)
                return
            else:
                currentNode = node
                while currentNode.rchild is not None:
                    currentNode = currentNode.rchild
                print(currentNode.key)
        maxNode(self)
        
    def delete(self,target):
        if self is None:
            print("BST is empty!")
            return
        if target < self.key:
            if self.lchild is None:
                print("Node not found!")
                return
            else:
                self.lchild.delete(target)
        elif target > self.key:
            if self.rchild is None:
                print("Node not found!")
                return
            else:
                self.rchild.delete(target)
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            current = self.rchild
            while current.lchild is not None:
                current = current.lchild
            self.key = current.key
            self.rchild = self.rchild.delete(self.key)
        print(self.key)
        
    def heightOfBST(self):
        queue = [self]
        height = 0
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelNode.append(currentNode.key)
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                if currentNode.rchild is not None:
                    queue.append(currentNode.rchild)
            height += 1
        print(height)
        
    
    def findDepth(self):
        if self.key is None:
            return
        
        lh = 0
        rh = 0
        if self.lchild is not None:
            lh = self.lchild.checkBalanced()
            if lh == -1:
                return -1
        if self.rchild is not None:
            rh = self.rchild.checkBalanced()
            if rh == -1:
                return -1
        if (abs(lh-rh)>1):
            return -1
        return 1 + max(lh,rh)
        
    def isBalanced(self):
        if self.findDepth == -1:
            print("Unbalanced")
        else:
            print("Balanced")
    
    def isSame(self,root2):
        root1 = self
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.key == root2.key and 
                (root1.lchild.isSame(root2.lchild) if root1.lchild and root2.lchild else root1.lchild == root2.lchild) and
                (root1.rchild.isSame(root2.rchild) if root1.rchild and root2.rchild else root1.rchild == root2.rchild))
    
    def zigZag(self):
        queue = [self]
        result = []
        index = 0
        while queue:
            levelSize = len(queue)
            levelNode = []
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                levelNode.append(currentNode.key)
                if currentNode.lchild is not None:
                    queue.append(currentNode.lchild)
                if currentNode.rchild is not None:
                    queue.append(currentNode.rchild)
                index += 1
            if index % 2 == 0:
                result.append(levelNode)
            else:
                levelNode.reverse()
                result.append(levelNode)
        print(result)
        
    
    def checkSymmetric(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.key == root2.key and (self.checkSymmetric(root1.lchild,root2.rchild) and (self.checkSymmetric(root1.rchild,root2.lchild))))
    
    def isSymmertic(self):
        if self is None:
            print("BST is empty!")
            return
        return self.checkSymmetric(self.lchild,self.rchild)
        
    
    
        
root = BST(None)
nums = [1,2,3]
for num in nums:
    root.insert(num)
root.traversal()
root.findMinAndMax()
root.delete(10)
root.heightOfBST()
root.isBalanced()

root2 = BST(None)
nums = [1,2,3,4]
for num in nums:
    root2.insert(num)
print(root.isSame(root2))
root.zigZag()
print(root.isSymmertic())