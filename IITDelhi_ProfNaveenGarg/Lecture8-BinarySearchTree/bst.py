class TreeNode:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

# class BinaryTree:

#     def __init__(self, root):
#         self.root = root

#     # def left(self, node):
#     #     return node.left
    
#     # def right(self, node):
#     #     return node.right
    
#     # def get_element(self, node):
#     #     return node.element

# recursive implementation of binary search tree
def BinarySearchTree_recur(node, k):
    if node is None: 
        print("Not found")
        return
    if k == node.element:
        print(f"{node.element} found")
        return node
    if k < node.element:
        return BinarySearchTree_recur(node.left, k)
    else:
        return BinarySearchTree_recur(node.right, k)
    
# iterative implementation of binary search tree
def BinarySearchTree_iter(node, k):
    while node and k != node.element:
        if k < node.element:
            node = node.left
        elif k > node.element:
            node = node.right
    return node

def BST_min(node):
    while node.left:
        node = node.left
    print(node.element)
    return node
    


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(4)
root.right = TreeNode(10)
root.right.left = TreeNode(7)
root.right.right = TreeNode(11)

# tree = BinaryTree(root)

target = 2
print(BinarySearchTree_recur(root, target))
print(BinarySearchTree_iter(root, target))

print(BST_min(root))






