#Write a Python program to sum of the first n positive integers

a=eval(input("Digite um valor: "))
soma_numero=(a*(a+1))/2

print(soma_numero)

#OU

b=eval(input("Digite o numero: "))
resultado=sum(range(b+1))
print(resultado)