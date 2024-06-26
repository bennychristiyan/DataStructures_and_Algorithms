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
#The recursive insert method has an additional parameter called currentnode, hence a normal insert method is also created to call the recursive
#insert method
    def __rinsert(self, currentnode, value):
        if currentnode == None:
            return Node(value)
        if value < currentnode.value:
            currentnode.left = self.__rinsert(currentnode.left, value)
        if value > currentnode.value:
            currentnode.right = self.__rinsert(currentnode.right, value)
        return currentnode

    def rinsert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__rinsert(self.root, value)
    
#2.Lookup method
#The recursive lookup method has an additional parameter called currentnode, hence a normal lookup method is also created to call the recursive
#lookup method
    def __rlookup(self, currentnode, value):
        if currentnode == None:
            return False
        if value == currentnode.value:
            return True
        if value < currentnode.value:
            return self.__rlookup(currentnode.left, value)
        if value > currentnode.value:
            return self.__rlookup(currentnode.right, value)

    def rlookup(self,value):
        return self.__rlookup(self.root, value)
    
#3.Delete method
#The recursive delete method has an additional parameter called currentnode, hence a normal delete method is also created to call the recursive
#delete method
    def __rdelete(self, currentnode, value):
        #If the node is not found in the BST
        if currentnode == None:
            return None
        #If the value is less than the currentnode value
        if value < currentnode.value:
            currentnode.left = self.__rdelete(currentnode.left, value)
        #If the value is greater than the currentnode value
        elif value > currentnode.value:
            currentnode.right = self.__rdelete(currentnode.right, value)
        #If the value is found in the BST
        else:
            #If the currentnode has no child nodes
            if currentnode.left == None and currentnode.right == None:
                return None
            #If the currentnode has no left subtree
            elif currentnode.left == None:
                currentnode = currentnode.right
            #If the currentnode has no right subtree
            elif currentnode.right == None:
                currentnode = currentnode.left
            #If the currentnode has subtrees on both sides: Find the minimum value in the right subtree, replace the value of currentnode with it 
            #and delete the minimum node in that subtree    
            else:
                min = self.min_value(currentnode.right)
                currentnode.value = min
                currentnode.right = self.__rdelete(currentnode.right, min)

        return currentnode

    def rdelete(self, value):
        self.__rdelete(self.root, value)

    def min_value(self, currentnode):
        while currentnode.left is not None:
            currentnode = currentnode.left
        return currentnode.value

my_tree = BinarySearchTree()

my_tree.rinsert(47)
my_tree.rinsert(21)
my_tree.rinsert(76)
my_tree.rinsert(18)
my_tree.rinsert(27)
my_tree.rinsert(52)
my_tree.rinsert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.rlookup(27))
print(my_tree.rlookup(17))

print(my_tree.min_value(my_tree.root))
print(my_tree.min_value(my_tree.root.right))

my_tree.rdelete(76)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

#Output
"""

47
21
76
True
False
18
52
47
21
82

"""

