"""Objective: Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and 
right children.

Method Signature:
def __invert_tree(self, node):

Input:
node: A Node object representing the root of a binary tree. The Node class has attributes value, left, and right, where value is the value stored in the node, and left and right are pointers to the node's left and right children, respectively.

Output:
The root node of the inverted binary tree.

Requirements:
The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.
If the input tree is empty (i.e., node is None), the method should return None.
The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.
The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
                  
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self.__invert_tree(node.left)
        self.__invert_tree(node.right)
        return node
            
        
        
        
        
          
        




#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result

def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")

test_invert_binary_search_tree()

#Output
"""

Empty Tree: Pass
Expected: []
Actual:   []

Single Node: Pass
Expected: [1]
Actual:   [1]

Tree with Left Child: Pass
Expected: [2, None, 1]
Actual:   [2, None, 1]

Tree with Right Child: Pass
Expected: [1, 2]
Actual:   [1, 2]

Multi-Level Tree: Pass
Expected: [3, 5, 1, None, None, 2]
Actual:   [3, 5, 1, None, None, 2]

Invert Twice: Pass
Expected: [4, 2, 6, 1, 3, 5, 7]
Actual:   [4, 2, 6, 1, 3, 5, 7]

"""