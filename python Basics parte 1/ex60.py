# Write a Python program to calculate the hypotenuse of a right angled triangle

from math import sqrt


def calcula(x,y):
    z=sqrt(x**2+y**2)
    return z

print(calcula(2,3))

a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero:"))

print(f"A soma dos quadrados dos catetos é igual a:",calcula(a,b))