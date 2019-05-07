# Outer class
class Student:
    def __init__ (self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show (self):
        print (self.name, self.rollno)
        self.lap.show()

    # Create another class laptop inside class Student
    # Inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'I5'
            self.ram = 5

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student ('Peter', 1)
s2 = Student ('Irene', 2)

s1.show()
s2.show()
# print ('s1.lap.brand: ', s1.lap.brand)
# lap1 = s1.lap
# lap2 = s2.lap
# print ('lap1.brand: ', lap1.brand)
# print ('lap2.brand: ', lap2.brand)