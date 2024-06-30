"""You have been given a string of lowercase letters.
Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table 
(dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the 
string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string."""

def first_non_repeating_char(string):
    alp_count = {}
    
    for letter in string:
        if letter in alp_count:
            alp_count[letter] += 1
        else:
            alp_count[letter] = 1
            
    for letter in string:
        if alp_count[letter] == 1:
            return letter
            
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )


#Output
"""

    l
    h
    None

"""