from abc import ABC, abstractmethod

# Define a TreeNode class to represent nodes in the binary tree
class TreeNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

# Define a BinaryTreetree class with some basic tree methods
class BinaryTreetree:
    def __init__(self, root):
        self.root = root

    def is_external(self, node):
        return node.left is None and node.right is None

    def left_child(self, node):
        return node.left

    def right_child(self, node):
        return node.right

    def get_element(self, node):
        return node.element

# Define TraversalResult class
class TraversalResult:
    def __init__(self):
        self.left_result = None
        self.right_result = None

# Define the abstract BinaryTreeTraversal class
class BinaryTreeTraversal(ABC):
    def __init__(self, tree):
        self.tree = tree

    def traverse_node(self, p):
        r = self.int_result()
        if self.tree.is_external(p):
            self.external(p, r)
        else:
            self.left(p, r)
            r.left_result = self.traverse_node(self.tree.left_child(p))
            self.below(p, r)
            r.right_result = self.traverse_node(self.tree.right_child(p))
            self.right(p, r)
        return self.result(r)

    @abstractmethod
    def int_result(self):
        pass

    @abstractmethod
    def external(self, p, result):
        pass

    @abstractmethod
    def left(self, p, result):
        pass

    @abstractmethod
    def below(self, p, result):
        pass

    @abstractmethod
    def right(self, p, result):
        pass

    @abstractmethod
    def result(self, result):
        pass

# Define a concrete PrintExpressionTraversal class
class PrintExpressionTraversal(BinaryTreeTraversal):
    def int_result(self):
        return TraversalResult()

    def external(self, p, result):
        print(p.element, end='')

    def left(self, p, result):
        print("(", end='')

    def below(self, p, result):
        print(p.element, end='')

    def right(self, p, result):
        print(")", end='')

    def result(self, result):
        return None
    
    def traverse(self):
        return self.traverse_node(self.tree.root)

# Create a sample binary tree
root = TreeNode("*")
root.left = TreeNode("+")
root.right = TreeNode("-")
root.left.left = TreeNode("3")
root.left.right = TreeNode("5")
root.right.left = TreeNode("8")
root.right.right = TreeNode("2")

# Create a BinaryTreetree instance with the root
tree = BinaryTreetree(root)

# Create a PrintExpressionTraversal instance and perform the traversal
expression_traversal = PrintExpressionTraversal(tree)
expression_traversal.traverse()  # Output: (3+5)-(8*2)
