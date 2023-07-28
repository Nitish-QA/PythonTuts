'''
When a class is derived from more than one base class it is called multiple Inheritance. 
The derived class inherits all the features of the base case.

'''
# Multiple Inheritance using two classes:

class Father():
    def Driving(self):
        print("Father Enjoys Driving")

class Mother():
    def Cooking(self):
        print("Mother is Cooking")

    def Driving(self):
        print("Mother Enjoys Driving")

class Child(Father, Mother):
    def Playing(self):
        print("Child Loves Playing")
c = Child()
c.Driving()  # Output: Father Enjoys Driving
c.Cooking()  
c.Playing()  # Output: Child Loves Playing

'''
Note:
1. 
This is not diamond problem, as their is no common anncestor with conflicting ancestor name

2.
In the code you provided, the Child class inherits from both the Father and Mother classes. 
When you call the Driving method on an instance of the Child class, 
Python looks for the method in the class hierarchy from left to right

Since Father is specified before Mother in the class declaration of Child:
Python will use the method from the Father class if it finds a method with the same name 


'''