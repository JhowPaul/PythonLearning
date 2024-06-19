#Write a Python program to determine whether variable is defined or not

try:
    x=1
except NameError:
    print("Variavel não foi definida")
else:
    print("Variavel foi definida")

try:
    y
except NameError:
    print("Variavel não definida")
else:
    print("Variavel foi definida")