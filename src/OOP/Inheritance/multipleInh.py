class A:
    varA=print("Welcome to class A")
class B:
    varB=print("Welcome to class B")
class C(A, B):
    varC=print("Welcome to class C")
c1 = C()
c1.varA
c1.varB
c1.varC