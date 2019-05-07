class A:
    def __init__ (self):
        print ('In A Init')

    def feature1 (self):
        print ("Feature 1 working")
    def feature2 (self):
        print ("Feature 2 working")

# B inheritance A
class B (A):
    def __init__ (self):
        # print inherit A here
        super(B, self).__init__()
        # print B here
        print ('In B Init')

    def feature3 (self):
        print ('Feature 3 working')
    def feature4 (self):
        print ('Feature 4 working')

# Class C
class C:
    def __init__ (self):
        print ('In C Init')

    def feature3 (self):
        print ('Feature 3 working')
    def feature4 (self):
        print ('Feature 4 working')

class D (A, C):
    def __init__ (self):
        # Need the MRO (Method Resolution Order). Print A only.
        super(D, self).__init__()
        # print B here
        print ('In D Init')

    def feature5 (self):
        print ('Feature 5 working')

print ('a1')
b1 = B()
print ('d1')
d1 = D()