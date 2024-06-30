#Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False 
#otherwise.
#For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False

def has_unique_chars(s):
    # Use a set to keep track of unique characters
    unique_chars = set()
    for char in s:
        # If the character is already in the set, it's not unique
        if char in unique_chars:
            return False
        # Otherwise, add it to the set
        unique_chars.add(char)
    # If we reach here, all characters are unique
    return True




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False


#Output
"""

    True
    False
    True
    True
    False

"""