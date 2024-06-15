#Write a Python program that will accept the base and height of a triangle and compute the area.

def triangulo(b,al):
    
    a=b*al/2
    return a

print(triangulo(20,40))

#OU
b = int(input("Insira a base : "))
h = int(input("Insira a altura : "))

area = b*h/2

print("area = ", area)
