#Write a Python program to calculate sum of digits of a number.
a=input("Insira uma sequencia de numeros: ")
soma=0
for i in a:
    soma+=int(i)
    print(soma)