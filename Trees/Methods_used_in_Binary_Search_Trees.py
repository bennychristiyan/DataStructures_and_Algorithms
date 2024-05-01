class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Constructor
class BinarySearchTree:
    def __init__(self):
        self.root = None
#1.Insert method          
    def insert(self, value):
        #Creating a new node
        new_node = Node(value)
        #If the tree is empty, the new node is made as the root node
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            #If the new node is already inside the tree, it returns False ending the while loop
            if new_node.value == temp.value:
                return False
            #If the new node is less than the temp and there is no node present at left of temp, the new node is inserted at left 
            #If the new node is less than the temp and there is a node present at left of temp, the left node of temp is made as new temp  
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            #If the new node is greater than the temp and there is no node present at right of temp, the new node is inserted at right 
            #If the new node is greater than the temp and there is a node present at right of temp, the right node of temp is made as new temp
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

#2.Lookup method
    def lookup(self, value):
        #We don't need to check if the tree is empty, because if the tree is empty, temp would be equal to None. Hence, while condition won't be satisfied and returns False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: 
                return True
        return False

my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.lookup(27))
print(my_tree.lookup(17))

#Output
"""

47
21
76
True
False

"""