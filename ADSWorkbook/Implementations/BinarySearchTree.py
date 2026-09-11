root=None
class BST:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None
    def traverse(val, node: BST = None):               #Incomplete
        global root
        if node == None: node = root 
        if node.value > val:
            if node.left != None:
                return traverse(val, node.left)
            else:
                return node
        elif node.value < val:
            if node.right != None:
                return traverse(val, node.right)
            else:
                return node
        else:
            return None
    def insert(val):                            #Incomplete
        newnode = BST(val)
        parentnode = traverse(val)
        if parentnode.value < val:
            newnode.parent = root
    def delete(val):
        pass