class Cookie:
    def __init__(self , color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def change_color(self , color):
        self.color = color

cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print("Cookie one is ", cookie_one.get_color())
print("Cookie two is ", cookie_two.get_color())

cookie_one.change_color("purple")

print("Cookie one is ", cookie_one.get_color())
print("Cookie two is ", cookie_two.get_color())

# output
"""

Cookie one is  green
Cookie two is  blue
Cookie one is  purple
Cookie two is  blue

"""