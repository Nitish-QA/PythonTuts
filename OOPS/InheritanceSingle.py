'''
Inheritance is the capability of one class to derive or inherit the properties from another class

'''

# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):   # this is abstract method which has no implementation, so we write 'pass'
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)         # Output: Buddy
print(dog.make_sound()) # Output: Woof!

'''
ANOTHER EXAMPLE WITH MAIN CLASS

'''
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")

# Derived class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the base class (Animal)
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")


def main():
    # Create an instance of the Dog class
    dog_instance = Dog("Buddy", "Golden Retriever")

    # Access methods from the base class (Animal)
    dog_instance.speak()

    # Access method from the derived class (Dog)
    dog_instance.bark()

if __name__ == "__main__":
    main()
'''
The code block if __name__ == "__main__": is a common Python idiom used to ensure that 
 a specific block of code is executed only when the Python script is run directly and not when 
it's imported as a module in another script.
'''