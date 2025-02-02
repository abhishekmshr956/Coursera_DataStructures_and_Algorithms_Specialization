class TreeNode:

    def __init__(self, element):
        self.element = element
        self.parent = None
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

def BST_max(node):
    while node.right:
        node = node.right
    print(node.element)
    return node

def BST_successor(node):
    if node.right:
        return BST_min(node.right)
    y = node.parent
    while y and node == y.right:
        node = y
        y = node.parent
    return y if y else None

#TODO: BST insertion
def BST_insertion(root, z):
    y = None
    x = root
    while x: # and x.element != z.element:
        y = x
        if z.element < x.element:
            x = x.left
        elif z.element > x.element:
            x = x.right
    z.parent = y
    if y is None:
        root = z
        # if root.element < z.element:
        #     z.left = root
        # elif root.element > z.element:
        #     z.right = root
    else:
        if z.element < y.element:
            y.left = z
        elif z.element > y.element:
            y.right = z

    


root = TreeNode(5)
root.left = TreeNode(3)
root.left.parent = root
root.left.left = TreeNode(2)
root.left.left.parent = root.left
root.left.right = TreeNode(5)
root.left.right.parent = root.left
root.left.right.left = TreeNode(4)
root.left.right.left.parent = root.left.right
root.right = TreeNode(10)
root.right.parent = root
root.right.left = TreeNode(7)
root.right.left.parent = root.right
root.right.right = TreeNode(11)
root.right.right.parent = root.right

# tree = BinaryTree(root)

target = 9
print(BinarySearchTree_recur(root, target))

new_node = TreeNode(target)
BST_insertion(root, new_node)

# target = 8
print(BinarySearchTree_recur(root, target))
print(BinarySearchTree_recur(root, target).parent.element)

# target = 11
# print(BinarySearchTree_recur(root, target))
# print(BinarySearchTree_iter(root, target))

# print(BST_min(root))
# print(BST_max(root))

# # given_node = BinarySearchTree_iter(root, target)
# given_node = root.right.right
# successor = BST_successor(given_node)
# # print(successor)
# # print(successor.element)
# if successor:
#     print(successor.element)
# else:
#     print("No successor")













