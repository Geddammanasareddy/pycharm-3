import add
def readvalue(v):
    print("enter two values for performing {}".format(v))
    h,b=int(input()),int(input())
    return h,b
def addition():
    h,b=readvalue("addition of two numbers")
    print("adding of numbers:({},{})={}".format(h,b,h+b))
def subtraction():
    h,b=readvalue("subtraction of two numbers")
    print("subtraction of ({},{})={}".format(h,b,h-b))
def multiplication():
    h,b=readvalue("subtraction of two numbers")
    print("multiplicate of ({},{})={}".format(h,b,h*b))
def division():
    h,b= readvalue("division of two numbers")
    print("division of ({},{})={}".format(h,b, h%b))
def modules():
    h,b= readvalue("modules of two numbers")
    print("moduls of ({},{})={}".format(h,b,h//b))

