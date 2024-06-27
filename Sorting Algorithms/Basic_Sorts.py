#1.Bubble Sort
#It places the Largest element in the list in it's correct position after each pass
#The original list also sorted after sorting
def BubbleSort(my_list):
    #The number of iterations reduce by 1 after each pass
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

originallist = [4,2,6,5,1,3]
sortedlist = BubbleSort(originallist)

print("Original list: ", originallist)
print("Sorted list: ", sortedlist)

#Output
"""

Original list:  [1, 2, 3, 4, 5, 6]
Sorted list:  [1, 2, 3, 4, 5, 6]

"""

#2.Selection Sort
#It places the Smallest element in the list in it's correct position after each pass
#The original list also sorted after sorting
def SelectionSort(my_list):
    for i in range(len(my_list)):
        min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] <  my_list[min]:
                min = j
        #If i is not equal to min, then jth and minth element are swapped
        if i != min:
            temp = my_list[i]
            my_list[i] = my_list[min]
            my_list[min] = temp
    return my_list        

originallist = [4,2,6,5,1,3]
sortedlist = SelectionSort(originallist)

print("Original list: ", originallist)
print("Sorted list: ", sortedlist)

#Output
"""

Original list:  [1, 2, 3, 4, 5, 6]
Sorted list:  [1, 2, 3, 4, 5, 6]

"""

#3.Insertion Sort
#The list has 2 parts; Ordered(left) and Unordered(right). After each pass, each element in Unordered part is placed in the correct position in   
#the Ordered part of the list
#The original list also sorted after sorting
def InsertionSort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j >= 0:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

originallist = [4,2,6,5,1,3]
sortedlist = InsertionSort(originallist)

print("Original list: ", originallist)
print("Sorted list: ", sortedlist)

#Output
"""

Original list:  [1, 2, 3, 4, 5, 6]
Sorted list:  [1, 2, 3, 4, 5, 6]

"""