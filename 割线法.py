import math
while True:
    x = input("x = ")
    y = input("y = ")
    for i in range(10):
        z = y-(y*y*y-2*y-5)*(y-x)/(y*y*y-2*y-5-x*x*x+2*x+5)   #µü´ú¹«Ê½
        print z
        x = y
        y = z
