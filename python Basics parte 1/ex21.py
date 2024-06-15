#Write a Python program to count the number 4 in a given list.

lista=[1,2,3,4,5,6,7,8,9,4]


print(lista[3],lista[-1])

#OU

print("\nLista 2\n")
def conta(x):
    contar=0
    for i in x:
        if i==4:
            contar+=1
    return contar

print(conta([1,2,3,4,5,6]))
print(conta([4,7,9,8,4,4,]))

