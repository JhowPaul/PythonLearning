#Write a Python program to check if every consecutive sequence of zeroes is
#followed by a consecutive sequence of ones of same length in a given string. Return True/False.

numero = input("Insira uma sequencia de 0 e 1:")

x = numero.count("0")
y = numero.count('1')

mensagem = True if x==y else False

print(mensagem) 

#não funciona 100%