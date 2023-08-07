from add import arthimetic
from sec import addition,subtraction,multiplication,division,modules
def operation():
    while(True):
        arthimetic()
        ch=int(input("enter ur choice"))
        match(ch):
            case 1:
                addition()
            case 2:
                subtraction()
            case 3:
                multiplication()
            case 4:
                division()
            case 5:
                modules()
operation()