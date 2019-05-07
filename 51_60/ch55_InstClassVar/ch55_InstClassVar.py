# We have two namespace:
# one is class namespace
# another one is Object/Instance namespace
class Car:
    # This is the class variable (class namespace)
    # This belongs to class namespce
    wheels = 4
    def __init__(self):
        # These belong to instance namespace
        self.mil = 10       # Instance variable (Object/Instance namespace)
        self.com = "BMW"    # Instance variable
    
c1 = Car();
c2 = Car();
c1.mil = 8
c1.com = "Mercede"
# If you want to modify the class namespace.
Car.wheels = 3

print ('c1.com = ', c1.com, 'c1.mil = ', c1.mil, 'c1.wheels = ', c1.wheels)
print ('c2.com = ', c2.com, 'c2.mil = ', c2.mil, 'c1.wheels = ', c1.wheels)