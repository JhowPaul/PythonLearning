#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list
#  and a tuple with those numbers.
number=3,5,7,23

print(list(number))
print(tuple(number))

#OU
valor = input("Input some comma seprated numbers : ")
lista = valor.split(",")
tupla = tuple(lista)
print('List : ',lista)
print('Tuple : ',tupla)