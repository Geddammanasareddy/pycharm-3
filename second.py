import first
def readvalue(op):
    print("enter two values for performing:{}".format(op))
    l,b=int(input()),int(input())
    return l,b
def radius(op):
    print("enter a value for performing:{}".format(op))
    r=int(input())
    return r
def ms(op):
    print("enter a value for performing:{}".format(op))
    return ms
def circle():
    r=radius("Area of circle")
    print("enter a radius:({})={}".format(r,3.14*r))
def rectangle():
    l,b=readvalue("area of rectangle")
    print("enter values for performing:({},{})={}".format(l,b,l+b))
def triangle():
    l,b=readvalue("area of rectangle")
    print("enter values for performing:({},{})={}".format(l,b,0.5*l,b))
def square():
    a=ms("area of square")