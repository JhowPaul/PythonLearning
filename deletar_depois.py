lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
#print(lista[6])
#print(lista[14])
'''
lista2=[]
for valor in lista:
    if valor %2==0:
        lista2.append(valor)
print(lista2)        
'''
#lista.count(2)

'''nome=input(str("insira o nome: "))
sobrenome=input(str("insira o sobrenome: "))
idade=input(str("insira o idade: "))

print('\nseu nome é: {}\nseu sobrenome é : {}\na sua idade é: {}'.format(nome,sobrenome,idade))
'''
'''notas = [ int(input("Informe a nota "+str() ) ) for x in range(4) ]
print("Eis as notas", notas)
print("Eis a média", sum(notas)/4) 
'''
#print(sum(lista)/4)

negativo=0
for n in lista:
    if n <0:
        negativo += n
#print('A soma dos elementos negativos é igual a {}'.format(negativo))
#ou
'''soma_dos_negativos = sum(n for n in lista if n < 0)
print('A soma dos elementos negativos é igual a {}'.format(soma_dos_negativos))'''
#ou
#negativo = sum(filter(lambda n: n < 0, lista))







