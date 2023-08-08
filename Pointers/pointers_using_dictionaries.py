# dictinaries are mutable, which means their values can be changed
# and both dictionaries still point to same memory location

dict1 = {"value":11}
dict2 = dict1

# both dict1 and dict2 point to the same memory location

print("Befor dict2 is value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))

dict2["value"] = 22

# both dict1 and dict2 again point to the same memory location

print("\nAfter dict2 is value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))

"""dict2 = {"value":33}

# dict1 and dict2 point to different memory location

print("\nAfter dict2 is value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))"""

# output
"""

Befor dict2 is value is updated:
dict1 =  {'value': 11}
dict2 =  {'value': 11}

dict1 points to  2257145450240
dict2 points to  2257145450240

After dict2 is value is updated:
dict1 =  {'value': 22}
dict2 =  {'value': 22}

dict1 points to  2257145450240
dict2 points to  2257145450240

[[[[[
    After dict2 is value is updated:
    dict1 =  {'value': 22}
    dict2 =  {'value': 33}

    dict1 points to  2257145450240
    dict2 points to  2257146917824
]]]]]

"""