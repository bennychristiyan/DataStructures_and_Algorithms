#1.Constructor and Hash method

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    #Hash Function to generate the address for the key-value pair
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            #The number 23 is used, because it is a prime number. We can use any prime number for the calculation
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        #enumerate function returns the item's index number and it’s value in a list or tuple etc.
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table = HashTable()

my_hash_table.print_table()

#Output
"""

0 : None
1 : None
2 : None
3 : None
4 : None
5 : None
6 : None

"""

#2.Set item
#Sets an item in the hash table using hash function

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash    
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 2000)
my_hash_table.set_item("lumber", 1000)

my_hash_table.print_table()

#Output
"""

0 : None
1 : None
2 : None
3 : None
4 : [['bolts', 1400], ['washers', 2000]]
5 : None
6 : [['lumber', 1000]]

"""

#3.Get item
#Gets the value from the hash table using it's key

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash    
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 2000)

print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))

#Output:
"""

1400
2000
None

"""

#4.Keys method
#Returns all the keys in the hash table

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash    
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 2000)
my_hash_table.set_item("lumber", 1000)

print(my_hash_table.keys())

#Output
"""

['bolts', 'washers', 'lumber']

"""