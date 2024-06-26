class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

#PostOrder DFS uses Stack datastructure. It traversals the tree: left --> right --> root.
#The value of the node is added to the list only if both child nodes of that node are already traversed.
    def dfs_postorder(self):
        result = []
        
        def traverse(currentnode):
            if currentnode.left is not None:
                traverse(currentnode.left)
            if currentnode.right is not None:
                traverse(currentnode.right)
            result.append(currentnode.value)
        traverse(self.root)
        return result
    
my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_postorder())

#Output
"""

[18, 27, 21, 52, 82, 76, 47]

"""