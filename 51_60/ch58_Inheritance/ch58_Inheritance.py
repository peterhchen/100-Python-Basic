class A:
    def feature1 (self):
        print ("Feature 1 working")
    def feature2 (self):
        print ("Feature 2 working")

# B inheritance A
class B (A):
    def feature3 (self):
        print ('Feature 3 working')
    def feature4 (self):
        print ('Feature 4 working')

# class C inherit B and A
class C (B):
    def fearure5(self):
        print ('Feature 5 working')

# class D inherit B and A
class D (B, A):
    def fearure5(self):
        print ('Feature 5 working')

print ('class A')
a1 = A(); a1.feature1(); a1.feature2()

# b1 want to inherit both class A and class B.
print ('class B')
b1 = B(); b1.feature1(); b1.feature2(); b1.feature3(); b1.feature4()

# class C inherit B, B inherit A
print ('class C')
c1 = C(); c1.feature1(); c1.feature2()
c1.feature3(); c1.feature4(); c1.fearure5()

# class D inherit A and B together
print ('class D')
d1 = D(); d1.feature1(); d1.feature2()
d1.feature3(); d1.feature4(); d1.fearure5()