#Write a Python program to sum of two given integers. 
#However, if the sum is between 15 to 20 it will return 20

def somaDois(x,y):
    z=x+y
    if z in range(15, 20):
        z=20
    return z

print("O soma de 2 e 3 é: ",somaDois(2,3))
print("O soma de 10 e 5 é: ",somaDois(10,5))

valor1=eval(input("Digite o primeiro valor: "))
valor2=eval(input("Digite o segundo valor: "))
print(f"A soma de {valor1} e {valor2} é: ",somaDois(valor1,valor2))