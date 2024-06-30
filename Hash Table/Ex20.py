#Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the 
#two lists, False otherwise.
#Use a dictionary to solve the problem that creates an O(n) time complexity.

def item_in_common(list1, list2):
    dic = {}
    for i in list1:
        dic[i] = True
        
    for j in list2:
        if j in dic:
            return True
            
    return False




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))


#Output
"""

    True

"""