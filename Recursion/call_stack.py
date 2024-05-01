def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne()

#Output
"""

Three
Two
One

"""

#Calling order

#1.funcOne() - pushed into stack (line 12)
#2.funcTwo() - pushed into stack (line 9)
#3.funcThree() - pushed into stack (line 5)
#4.print("Three") (line 2)
#5.funcThree() - popped out of stack (line 5)
#6.print("Two") (line 6)
#7.funcTwo() - popped out of stack (line 9)
#8.print("One") (line 10)
#9.funcOne() - popped out of stack (line 12)