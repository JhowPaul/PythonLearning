#Write a Python program to get the volume of a sphere with radius 6.
from math import pi

r=0
def raio(r):
    r=6

    v=4/3*pi*r**3
    print(f"o volume da esfera é: {v}")

raio(r)