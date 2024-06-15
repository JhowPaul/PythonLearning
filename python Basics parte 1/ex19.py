#Write a Python program to get a string which is n (non-negative integer) copies of a given string

dado=input("digite algo:")

for info in range(3):
    print(dado)

#OU
def copia(texto,a):
    arq=""
    for i in range(a):
        arq+=texto
    return arq

print(copia('abc',2))
print(copia('teste',3))