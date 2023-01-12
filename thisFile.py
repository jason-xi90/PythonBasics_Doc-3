from math import pi as p

def thisarea():
    length = input("Please type in the length:")
    width = input("Please type in the width:")
    Area = float(length) * float(width)
    return Area
print(thisarea())

def thiscircumference():
    radius = input("Please type in the radius:")
    Circumference = 2*p*float(radius)
    return Circumference
print(thiscircumference())