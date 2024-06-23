triangleside1 = 60
triangleside2 = 60
triangleside3 = 60

if(triangleside2 == triangleside1 and triangleside2 == triangleside3):
    print("Equilateral")
elif((triangleside2 == triangleside1 or triangleside2 == triangleside3 or triangleside1 == triangleside3) and (triangleside1 != triangleside2 or triangleside2 !=  triangleside3 or triangleside1 != triangleside3)):
    print("Isocele")
elif(triangleside1 != triangleside2 and triangleside2 !=  triangleside3 and triangleside1 != triangleside3):
    print("Scalene")