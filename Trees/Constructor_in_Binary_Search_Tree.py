class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Constructor with a root node when creating a tree
class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
my_tree = BinarySearchTree(5)

print(my_tree.root.value)

#Constructor without a root node when creating a tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

my_tree = BinarySearchTree()

print(my_tree.root)

#Output
"""

5
None

"""