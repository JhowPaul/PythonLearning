#Write a Python program to remove the first item from a specified list

lista=[1,2,3,4,5,6,7,8]

del lista[0]
print(lista)

nomes=["Joao","Paulo","Gomes","Pereira"]
nomes.remove("Gomes")
print(nomes)

frase=input("Insira uma frase: ").split()
del frase[2]
print(frase)