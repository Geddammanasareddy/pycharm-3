from first import area
from second import circle,rectangle,triangle,square
def operations():
    while(True):
        area()
        ch=int(input("enter ur choice:"))
        match(ch):
            case 1:
                circle()
            case 2:
                rectangle()
            case 3:
                triangle()
            case 4:
                square()
            case 5:
                print("thnx for using program")
            case _:
                print("ur selection")
operations()