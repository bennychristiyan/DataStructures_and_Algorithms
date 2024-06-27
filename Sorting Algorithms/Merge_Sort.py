#The original list remains the same after sorting
#1.Merge Sort method
#This method divides the list into small lists with only one element in them
def MergeSort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    left = MergeSort(my_list[:mid])
    right = MergeSort(my_list[mid:])
    return merge(left, right)

#2.Merge method
#This method combines 2 sorted lists together to form a combined sorted list. We do this process until the entire original list is sorted
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

originallist = [4,2,6,5,1,3]
sortedlist = MergeSort(originallist)

print("Original list: ", originallist)
print("Sorted list: ", sortedlist)

#Output
"""

Original list:  [4, 2, 6, 5, 1, 3]
Sorted list:  [1, 2, 3, 4, 5, 6]

"""
    