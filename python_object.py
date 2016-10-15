class A(object):
    def speek(self):
        print("AAAAAAAAAAA")

class B(A):
    pass

class C(A):
    def speek(self):
        print('CCCCCCC')

class D(B):
    pass

d = D()
d.speek()
