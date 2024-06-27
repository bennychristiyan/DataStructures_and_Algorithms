#The original list also sorted after sorting
#1.Pivot method
#This method places the pivot element at it's correct position in the list. The elements that are less than the value of pivot element are 
#placed left to pivot element and the and the elements that are greater than the value of pivot element are placed right to pivot element
def pivot(my_list, p, end):
    swap = p
    for i in range(p+1, end+1):
        if my_list[i] < my_list[p]:
            swap += 1
            my_list[i], my_list[swap] = my_list[swap], my_list[i]
    my_list[p], my_list[swap] = my_list[swap], my_list[p]
    return swap

#2.Quick sort method
#This method does quick sort to the left part and right part to the pivot element
def __QuickSort(my_list, left, right):
    if left < right:
        p = pivot(my_list, left, right)
        __QuickSort(my_list, left, p-1)
        __QuickSort(my_list, p+1, right)
    return my_list

def QuickSort(my_list):
    return __QuickSort(my_list, 0, len(my_list)-1)

originallist = [4, 2, 7, 6, 5, 1, 3]
sortedlist = QuickSort(originallist)

print("Original list: ", originallist)
print("Sorted list: ", sortedlist)

#Output
"""

Original list:  [1, 2, 3, 4, 5, 6, 7]
Sorted list:  [1, 2, 3, 4, 5, 6, 7]

"""