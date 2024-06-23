triangleside1 = int(input("Type the size of the triangle side 1: "))
triangleside2 = int(input("Type the size of the triangle side 2: "))
triangleside3 = int(input("Type the size of the triangle side 3: "))
if(triangleside3 + triangleside2 + triangleside1 == 180 and triangleside1 > 0 and triangleside2>0 and triangleside3>0 and triangleside1< triangleside2 + triangleside3 and triangleside2< triangleside3 + triangleside1 and triangleside3< triangleside2+triangleside1):
    if(triangleside2 == triangleside1 and triangleside2 == triangleside3):
        print("Equilateral")
    elif((triangleside2 == triangleside1 or triangleside2 == triangleside3 or triangleside1 == triangleside3) and (triangleside1 != triangleside2 or triangleside2 !=  triangleside3 or triangleside1 != triangleside3)):
        print("Isocele")
    elif(triangleside1 != triangleside2 and triangleside2 !=  triangleside3 and triangleside1 != triangleside3):
        print("Scalene")
else:
    print("Not a triangle.")