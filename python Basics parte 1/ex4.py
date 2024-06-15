import cmath  #Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi

r=0
def raiocirculo(r):
    b=cmath.pi*r**2
    return b

print(raiocirculo(1))

#OU
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))