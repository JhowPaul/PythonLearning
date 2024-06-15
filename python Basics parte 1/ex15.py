#Write a Python program to test whether a number is within 100 of 1000 or 2000.
#abs retorna o valor absoluto
def pertoDeMil(n):
    return ((abs(1000-n)<=100)or(abs(2000-n)<=100))#se numero entre 100 e 1000 ou 2000 e 100

print(pertoDeMil(1000))
print(pertoDeMil(900))
print(pertoDeMil(800))
print(pertoDeMil(2200))

#sem o abs
print("\n")
def pertoDeMil(m):
    return ((1000-m)<=100)or((2000-m)<=100)#se numero entre 100 e 1000 ou 2000 e 100

print(pertoDeMil(1000.40))
print(pertoDeMil(900))
print(pertoDeMil(800))
print(pertoDeMil(2000))