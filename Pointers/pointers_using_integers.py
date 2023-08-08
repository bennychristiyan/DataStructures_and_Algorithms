# integers are immutable, which means they can't be changed
# but we can use the variable to point another number stored in another location

num1 = 11
num2 = num1

# both num1 and num2 point to the same memory location

print("Befor num2 is value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to ", id(num1))
print("num2 points to ", id(num2))

num2 = 22

# num1 and num2 point to different memory location

print("\nAfter num2 is value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to ", id(num1))
print("num2 points to ", id(num2))

# output
"""

Befor num2 is value is updated:
num1 =  11
num2 =  11

num1 points to  140722018120808
num2 points to  140722018120808

After num2 is value is updated:
num1 =  11
num2 =  22

num1 points to  140722018120808
num2 points to  140722018121160

"""