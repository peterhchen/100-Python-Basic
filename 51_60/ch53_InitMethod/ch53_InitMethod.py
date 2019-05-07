# We have variables and methods in the class.

class Computer:
    # Attributes: Variables RAM and CPU
    # self is passed automatically.
    # __init__ method is constructor in C++/Java
    def __init__ (self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    # Behavior: Methods (Funcitons)
    def config (self):
        print ("self.cpu = ", self.cpu, 'self.ram = ', self.ram)
 
# Every objects have their own variables and methods.  
com1 = Computer('I5', 16)
com2 = Computer('I7', 20)
com1.config()
com2.config()