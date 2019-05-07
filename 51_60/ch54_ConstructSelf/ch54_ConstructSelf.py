# This section is for Constructor and self.
# __init__ is a constructor
# self is a pointer to point c1 or c2 object.

class Computer:
    # pass tell compilier to ignore the rest of code.
    #pass 
    # __init__ method is constructor in C++/Java
    def __init__ (self, cpu, ram):
        self.name = 'Peter Home'
        self.cpu = cpu
        self.ram = ram
 
    def update (self, name):
        self.name = name

    def compare (self, other):
        # c1 become self
        if (self.name == other.name):
            return True
        else:
            return False

# self assign to c1 object
c1 = Computer('I5', 16)
c1.name = 'Irene'
# self assigb to c2 object
c2 = Computer('I7', 20)
c2.update ('Jonathan')
# Print id or address of the object located somewhere in the heap memory.
print ('id(c1) = ', id (c1))
print ('id(c2) - ', id (c2))
print ('c1.name = ', c1.name)
print ('c2.name = ', c2.name)

#if (c1 == c2):
# compare is not a embeded funciton. You have to define your own.
c1.update ('Jonathan')
if (c1.compare (c2)):
    print ('c1 and c2 are the same')