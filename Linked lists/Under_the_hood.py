# The nodes in Linked lists are similar to a dictionary which has value(data) and next(pointer) as keys
linked_list = {
                "value": 11,
                "next": {
                        "value": 3,
                        "next": {
                                "value": 23,
                                "next": {
                                        "value": 7,
                                        "next": None
                                        }
                                }
                        }
                } 
print(linked_list["next"]["next"]["value"])

# This will only run with a linked list
# print(my_linked_list.linked_list.next.next.value)

# Output
"""

23

"""