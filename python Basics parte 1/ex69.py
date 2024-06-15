#Write a Python program to sort three integers without using conditional statements and loops.

a=int(input("Insira o primeiro numero: "))
b=int(input("Insira o segundo numero: "))
c=int(input("Insira o terceiro numero: "))

maximo=max(a,b,c)
minimo=min(a,b,c)
meio=(a+b+c) - maximo-minimo
print("A ordem é: ",minimo,meio,maximo)