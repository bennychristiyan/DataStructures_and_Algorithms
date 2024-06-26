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
                
#BFS uses Queue datastructure. It traversals the tree, level by level (i.e) It visits both child nodes of a node at a time
    def BFS(self):
        currentnode = self.root
        queue = []
        result = []
        queue.append(currentnode)
        while len(queue) > 0:
            currentnode = queue.pop(0)
            result.append(currentnode.value)
            if currentnode.left is not None:
                queue.append(currentnode.left)
            if currentnode.right is not None:
                queue.append(currentnode.right)
        return result

my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())

#Output
"""

[47, 21, 76, 18, 27, 52, 82]

"""