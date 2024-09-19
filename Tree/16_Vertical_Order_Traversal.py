class BST:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

    def verticalOrder(self, root, h_dist, v_dist, values):
        # Base case: if the root is None, return
        if not root:
            return

        # Add the node to the dictionary with its horizontal and vertical distance
        if h_dist in values:
            values[h_dist].append((v_dist, root.val))
        else:
            values[h_dist] = [(v_dist, root.val)]

        # Recur for left subtree with horizontal distance - 1 and vertical distance + 1
        self.verticalOrder(root.lchild, h_dist - 1, v_dist + 1, values)

        # Recur for right subtree with horizontal distance + 1 and vertical distance + 1
        self.verticalOrder(root.rchild, h_dist + 1, v_dist + 1, values)

    
    def verticalTraversal(self):
        values = {}
        self.verticalOrder(self, 0, 0, values)
        sorted_values = sorted(values.items())

        result = []
        # For each horizontal distance, sort nodes by vertical distance and append to result
        for h_dist, nodes in sorted_values:
            nodes.sort()  # Sort by vertical distance first
            result.extend([val for v_dist, val in nodes])
        
        print(result)
        return
    
    '''
    def verticalTraversal(self):
            values = {}
            result = []
            self.verticalOrder(self,0,0,values)
            sorted_values = sorted(values)
            for value in sorted_values:
                values[value].sort()
                node = values[value]
                for n in node:
                    result.append(n[1])
            print(result)
    '''



# Create the tree
root = BST(1)
root.lchild = BST(2)
root.lchild.lchild = BST(3)
root.lchild.rchild = BST(4)
root.rchild = BST(5)
root.rchild.lchild = BST(6)

root.verticalTraversal()