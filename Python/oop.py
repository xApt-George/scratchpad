# This page was built from watching the Soratica youtube channel
# https://www.youtube.com/watch?v=0XR_91AfgZI&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=52

# Class attributes:    belong to the class
#                      and are shared among all objects
# Instance attributes: belong to object
#                     - They are attached to self
#                     - Not available to class
# Class methods:      @class method decorator,
#                     Can be called by an object or the class
#                     The class argument cls is passed implicitly
# Instance methods:   have access to all class things
#                     and instance things

# Define class
class Person:
    counter = 0 # Class attribute, number of Person objects

    def __init__(self, name):
        self.full_name = name  # Instance attribute
        Person.counter += 1    # Increment the class attribute
    
    def introduction(self):
        print(self)   # Prints an object of type person
        # Instance method uses self to access the instance attributes
        print(f"\nHello! My name is {self.full_name}.")
    
    @classmethod
    def population(cls):
        # Class method uses cls to access the class attribute
        print(f"The current population is {cls.counter}")

p1 = Person("Batman")
print(f'Full name = {p1.full_name}')
p1.introduction()  # Calling an instance method
p1.population()    # Calling a class method via an instance

p2 = Person("Robin")
print(f'Full name = {p1.full_name}')
p2.introduction()
Person.population()  # Calling a class method via the class

# Monkey patching - dynamically attaching an attribute or method to 
#                   an object is called monkey patching.
# Attach a coin attribute to p1
p1.coin = 1618033

# Attach version attribute to class
Person.version = 1.0

print("\n", dir(p1))        # You'll notice coin exists in this object
print("\n", dir(p2))        # But won't exist in this object
print("\n", dir(Person))    # coin won't exist in the class either
                            # version will exists in all 3 print lines