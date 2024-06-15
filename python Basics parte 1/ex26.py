#Write a Python program to concatenate all elements in a list into a string and return it.

def concatenar(x):
    resultado=''
    for i in x:
        resultado+=str(i)
    return resultado

print(concatenar([1,2,3,4,5,6,7]))