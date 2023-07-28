class Details():
    name = 'Rohit'
    place = 'Mumbai'


print(Details.name)


# 'SELF' parameter is similar to this
# __init__ is used for creating constructor
# lets create another class
class car():
      
    # __init__ method or constructor
    def __init__(self, model, color):    
        self.model = model
        self.color = color
          
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )

# Now here we created two objects of car class with some parameters
# NOTE: we are only passing two parameters, self is autocalled
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()
ferrari.show()

'''
self is parameter in Instance Method and user can use another parameter name in place of it. 
But it is advisable to use self because it increases the readability of code, 
and it is also a good programming practice.

'''

'''
The __init__ method is similar to constructors in C++ and Java. 
It is run as soon as an object of a class is instantiated. 
Lets' see example
'''
class Dog:
    name = 'Rocky'

    def __init__(self):      # We must have to write self even for no parameter
        print(f'Hello {self.name}')

obj1 = Dog()  # We don't need 'new' keyword like other prog. lang.
# this will directly call the class constructor

print(Dog.name) # we can access class variables







