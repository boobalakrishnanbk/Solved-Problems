# binary tree traversal
class Tree:
    def __init__(self, value = None) -> None:
        self.left = None
        self.right = None
        self.value = value

    # insert root
    def insertValue(self, value) -> None:
        if self.value: # check if root has value
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insertValue(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insertValue(value)
            
        else: # assign root value if not assigned
            self.value = value

    def PrintTree(self, orderTraversal = "PREORDER") -> None:        
        if orderTraversal.upper().replace(" ","") == "PREORDER": print(self.value, end = " ")
        if self.left:
            self.left.PrintTree(orderTraversal)
        if orderTraversal.upper().replace(" ","") == "INORDER": print(self.value, end = " ") 
        if self.right:
            self.right.PrintTree(orderTraversal)
        if orderTraversal.upper().replace(" ","") == "POSTORDER": print(self.value, end = " ")
        return None

binaryTree = Tree()
insertInputs = [27,14,11,42,35,19,31,9,10, 10]
for i in insertInputs:
    binaryTree.insertValue(i)
'''type the type of traversal order'''
binaryTree.PrintTree(orderTraversal="")

# print(binaryTree.PreOrderTraversal(binaryTree))    ''' another way of traversing '''
'''
def PreOrderTraversal(self, tree) -> list:
    outputValue = []
    if tree:
        outputValue.append(tree.value)
        outputValue += self.PreOrderTraversal(tree.left)
        outputValue += self.PreOrderTraversal(tree.right)
    return outputValue

    def LeftOrderTree(tree) -> List:
        return self.PreOrderTraversal(tree.left)
'''