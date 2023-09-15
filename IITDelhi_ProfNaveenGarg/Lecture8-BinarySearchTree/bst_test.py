class TreeNode:
    def __init__(self, element):
        self.element = element
        self.parent = None
        self.left = None
        self.right = None

def BST_successor(node):
    # If the node has a right child, find the minimum value in the right subtree.
    if node.right:
        return BST_min(node.right)
    
    # If the node doesn't have a right child, traverse up the tree to find the successor.
    # Initialize a variable to keep track of the parent node.
    parent = node.parent
    
    while parent is not None and node == parent.right:
        node = parent
        parent = parent.parent
    
    return parent

def BST_min(node):
    while node.left:
        node = node.left
    return node

# Example usage:
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

target = 11
given_node = root.right.right  # You can set this to the node you want to find the successor for
successor = BST_successor(given_node)

if successor:
    print(f"Successor of {given_node.element} is {successor.element}")
else:
    print(f"{given_node.element} is the maximum node, and it has no successor.")
