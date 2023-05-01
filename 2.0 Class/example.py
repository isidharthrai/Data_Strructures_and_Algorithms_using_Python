class Cookie:
    #constructor 
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    


#initializing via self keyword.
CookieOne = Cookie('red')
CookieTwo = Cookie('green')

print(CookieOne.get_color()) #red
print(CookieTwo.get_color()) #green

CookieOne.set_color('yellow')
CookieTwo.set_color('blue')

print(CookieOne.get_color()) #yellow
print(CookieTwo.get_color()) #blue