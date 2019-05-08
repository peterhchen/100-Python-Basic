# Type of variable of is a name of the memory
#x = 5
#x = 'Peter'
class PyCharm:
    def execute(self):
        print ("Compiling")
        print ("Running")

class MyEditor:
    def execute (self):
        print ("Spell Check")
        print ("Convention Check")
        print ("Compiling")
        print ("Running")

class Laptop:
    def code (self, ide):
        ide.execute();

ide = MyEditor()
print ('MyEditor:')
lap1 = Laptop()
lap1.code(ide)

print ('PyCharm:')
ide = PyCharm()
lap1.code (ide)