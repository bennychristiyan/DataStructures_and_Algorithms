"""Objective:
The task is to develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.
This involves creating a BST where the depth of the two subtrees of any node does not differ by more than one.
Achieving a height-balanced tree is crucial for optimizing the efficiency of tree operations, ensuring that the BST remains efficient for search, 
insertion, and deletion across all levels of the tree.

Method Overview: __sorted_list_to_bst

Input: A sorted list of integers nums, provided in ascending order. The input list represents a sequential collection of elements to be 
transformed into a BST. The method also receives two additional parameters, left and right, which denotes the current segment of the list being 
processed.

Process: The method __sorted_list_to_bst employs a divide-and-conquer strategy to construct the BST. It identifies the middle element of the 
current list segment to serve as the subtree's root, ensuring that the resulting BST is height-balanced. The method recursively applies this 
logic to the left and right halves of the list, building up the BST from the bottom up.

Output: The root node of a height-balanced BST constructed from the sorted list. This node links to all other nodes in the BST, effectively 
representing the entire tree structure

Requirements:
The BST must maintain the binary search tree property: for any given node, all values in the left subtree must be less than the node's value, and 
all values in the right subtree must be greater.
The resulting BST should be height-balanced to optimize the efficiency of subsequent operations performed on the tree."""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                
                
    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right)//2
        node = Node(nums[mid])
        node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        node.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        return node


#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")

# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = BinarySearchTree()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)

#Output
"""

Is balanced: True
Inorder traversal: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Expected traversal: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
PASS: Tree is balanced and inorder traversal is correct.

"""
