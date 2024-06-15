#Write a Python program to display your details like name, age, address in three different lines.

def informacao():
    nome,idade="Joao",24
    endereco="Rio de Janeiro,RJ,Brasil "
    print(f"Nome: {nome}\nIdade: {idade}\nEndereço: {endereco} ")

informacao()

nome=input("Insira o seu nome: ")
idade=input("Insira a idade: ")
endereco=input("Insira o endereço: ")

print(f"Nome: {nome}\nIdade: {idade}\nEndereço: {endereco}")
