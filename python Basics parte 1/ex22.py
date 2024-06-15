#Write a Python program to get the n (non-negative integer) copies of the first 2 characters 
#of a given string. Return the n copies of the whole string if the length is less than 2

def captura(pega,x):
    tamanho=2
    if tamanho>len(pega):
        tamanho=len(pega)
    recebe=pega[:tamanho]

    resultado=""
    for i in range(x):
        resultado+=recebe
    return resultado

print(captura("here is the house",2))
print(captura("Madness",8))

