# class with name "Computer"
# We have to specify ":"
class Computer:
    # ATtributes: Variables
    # Behavior: Methods (Funcitons)
    def config (self):
        print ("I5 machine, 16GB RAM, 1TB Stroage")
 

# We want to use a computer obj
# We have to define a class first with the name "Computer".
x = 9
print (type (x))
a = '8';
print (type (a))
# How do we call the method in the class?
com1 = Computer ()
com2 = Computer()
print (type (com1))
# First way
Computer.config(com1)
Computer.config(com2)
# Second way.
com1.config()
com2.config()