#Write a Python program to sum of three given integers. However, 
#if two values are equal sum will be zero.

def somaTres(x,y,z):
    w=x+y+z
    if x==y or y==z or x==z:
        w=0
   
    return w

print("O valor é: ",somaTres(2,3,4))
print("O valor é: ",somaTres(2,2,4))

#OU
def somaTres():
    x=eval(input("Insira o primeiro valor :"))
    y=eval(input("Insira o segundo valor: "))
    z=eval(input("Insira o terceiro valor: "))
    w=x+y+z
    if x==y or y==z or x==z:
        w=0
   
    return w


print("o Valor de  é: ",somaTres())