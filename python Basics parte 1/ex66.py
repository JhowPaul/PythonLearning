#Write a Python program to calculate body mass index

def imc(peso,altura):
    altura/=100
    imc=round(peso/(altura**2))
    return imc

print("O seu imc é: ",imc(60,180))

#OU
peso=float(input("Insira o seu peso: "))
altura=float(input("Insira a sua altura: "))/100

print("O seu imc é: ",round(peso/(altura**2)))

