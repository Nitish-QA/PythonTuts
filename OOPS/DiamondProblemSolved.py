'''
The diamond problem is a common issue that can occur in programming languages that 
support multiple inheritance. It arises when a class inherits from two or more classes 
that have a common ancestor. 

   A
  / \
 B   C
  \ /
   D
In this example, class D inherits from both classes B and C, which in turn both inherit from class A. 
This creates a diamond-shaped inheritance hierarchy. The problem arises when classes B and C have a 
method with the same name, let's say foo(). Now, when we call foo() on an instance of class D, 
it is ambiguous which version of foo() should be called: the one from class B or the one from class C.

Python provides a mechanism called Method Resolution Order (MRO) to solve this issue. 
The MRO determines the order in which Python searches for methods in a class hierarchy 
during method calls.

'''

class Grandparent():
    def Driving(self):
        print("Grandparent Enjoys Driving")

class Father(Grandparent):
    def Driving(self):
        print("Father Enjoys Driving")

class Mother(Grandparent):
    def Driving(self):
        print("Mother Enjoys Driving")

class Child(Father, Mother):
    def Playing(self):
        print("Child Loves Playing")

c = Child()
c.Driving()
c.Playing()

print('------------------------------------------------------')
# Access the MRO of class D
print(Child.__mro__)


