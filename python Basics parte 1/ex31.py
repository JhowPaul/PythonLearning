#Pass values from a list as method arguments
#We can extract all elements of a list using "*":

miha_lista = [1, 2, 3, 4]
print(miha_lista)  # [1, 2, 3, 4]

print(*miha_lista)  # 1 2 3 4

def soma_elementos(*arg):
    total = 0
    for i in arg:
        total += i

    return total


resultado = soma_elementos(*[1, 2, 3, 4])
print(resultado)  # 10

