# we have two variables: class and instance
# we have three methods: class, static, and instance.
class Student:
    # class variable
    school = "USC"

    # Instance method for instance variable
    # Use 'self' for instance method passing parameter
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    # Instance method for instance variable
    def avg (self):
        return (self.m1 + self.m2 + self.m3)/3

    # cls is passed class method
    # Use 'cls' for class mehod and vaiable.
    @classmethod
    def getSchool (cls):
        return (cls.school)

    # This is for 'static' method
    # There is no class varaible and no instance variable.
    @staticmethod
    def info (): 
        print ('This is for Student class ... in this module')

s1 = Student (50, 60, 70)
s2 = Student (70, 80, 90) 

print (Student.school, s1.m1, s1.m2, s1.m3, 's1.avg(): ', s1.avg())
# print the class method.
#print (s1.getSchool())
print (Student.getSchool())
Student.info()