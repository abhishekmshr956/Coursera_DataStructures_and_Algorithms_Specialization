class TreeNode:
    """ Node for a binary tree """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root == None:
        return
    else:
        print(root.value, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root == None:
        return
    else:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end = " ")

def inorder_traversal(root):
    if root == None:
        return
    else:
        inorder_traversal(root.left)
        print(root.value, end = " ")
        inorder_traversal(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Preorder Traversal")
preorder_traversal(root)
print("\nPostorder Traversal")
postorder_traversal(root)
print("\n")
print("Inorder Traversal")
inorder_traversal(root)

