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

#PreOrder DFS uses Stack datastructure. It traversals the tree: root --> left --> right
#The value of the node is added to the list, starting from the root node to the left child nodes. Once there is no left child node, it adds the     
#value of the right child node
    def dfs_preorder(self):
        result = []
        
        def traverse(currentnode):
            result.append(currentnode.value)
            if currentnode.left is not None:
                traverse(currentnode.left)
            if currentnode.right is not None:
                traverse(currentnode.right)

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

print(my_tree.dfs_preorder())

#Output
"""

[47, 21, 18, 27, 76, 52, 82]

"""